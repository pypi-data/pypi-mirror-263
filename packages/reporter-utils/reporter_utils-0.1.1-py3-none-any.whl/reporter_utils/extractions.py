"""
Bases for `extract` commands.
"""
from __future__ import annotations

import json as _json
import logging
import os
import re
import sys
from io import IOBase
from pathlib import Path
from types import ModuleType
from typing import Any, TypeVar

import yaml

from zut import ExtendedJSONEncoder, Header, OutTable, OutFile, normalize_out, Literal, get_config_paths

logger = logging.getLogger(__name__)


class Extraction:
    def __init__(self, key: str, definition_file: Path):
        self.name = key
        self.definition_file = definition_file
        
        with open(self.definition_file, 'r', encoding='utf-8') as fp:
            definition_dict: dict[str,Any] = yaml.safe_load(fp)
        if not isinstance(definition_dict, dict):
            raise ValueError(f"Definition file loaded as {type(definition_dict)}, expected dict")

        self.help: str|None = definition_dict.pop('help', None)
        self.type: str|list[str] = definition_dict.pop('type')
        self.tabulate: list[str] = definition_dict.pop('tabulate', None)

        self.root: FieldGroup = self._parse_field(definition_dict.pop('fields', {
            'name': 'name',
            'ref': 'ref',
            'overall_status': 'overallStatus',
            'config_status': 'configStatus',
        }), '')

        self.vars: dict[str,Field] = {}
        for key, value in  definition_dict.pop('vars', {}).items():
            self.vars[key] = self._parse_field(value, f'vars/{key}')

        self._resolved_vars: dict[str,dict[Any,Any]] = {}

        for key in definition_dict:
            logger.warning(f"Extraction {self.name}: ignore key {key}")


    def _parse_field(self, descr: dict|str, fullkey: str):
        if isinstance(descr, dict): # sub fields
            field = FieldGroup(fullkey)
            for subkey, subdescr in descr.items():
                if subkey == '_root':
                    field.root = self._parse_field(subdescr, f'{fullkey}/{subkey}')
                elif subkey == '_table':
                    field.table = self._parse_field(subdescr, f'{fullkey}/{subkey}')
                elif subkey.startswith('_'):
                    logger.warning(f"Extraction {self.name}: ignore {subkey}")
                else:
                    subfield = self._parse_field(subdescr, f"{fullkey + '/' if fullkey else ''}{subkey}")
                    if subfield:
                        field.fields[subkey] = subfield
            
            return field
            
        elif isinstance(descr, str):
            parts = descr.split(' ')
            attr = parts[0].strip()
            if not attr:
                logger.warning(f"Extraction {self.name}: ignore {fullkey}: invalid description: {descr}")
                return None            
            field = Field(fullkey, attr)
            
            for option in parts[1:]:
                m = re.match(r'^([^=]+)=(.+)$', option)
                if not m:
                    logger.warning(f"Extraction {self.name}: ignore invalid option for {fullkey}: {option}")
                    continue

                option_key = m[1].strip()
                option_value = m[2].strip()
                if not option_value:
                    continue

                if option_key == 'fmt':
                    field.fmt = option_value
                elif option_key == 'multiply':
                    field.multiply = float(option_value) if '.' in option_value else int(option_value)
                else:
                    logger.warning(f"Extraction {self.name}: ignore unknown option for {fullkey}: {option_key}")

            return field
        
        elif descr is None: # e.g. '_table: null'
            return Field(fullkey, None)

        else:
            logger.warning(f"Extraction {self.name}: ignore field {fullkey} (invalid type: {type(descr)})")
            return None


    def extract(self, out: os.PathLike|IOBase = None, extractfmt: Literal['json', 'csv', 'tabulate'] = None, top: int = None, **options):
        title = self.name
        out = normalize_out(out, title=title)

        if extractfmt is None:
            if not out or out == sys.stdout or out == sys.stderr:
                extractfmt = 'tabulate'
            else:
                lower_out = str(out).lower()
                if lower_out.endswith('.csv'):
                    extractfmt = 'csvx'
                elif lower_out.endswith('.xlsx'):
                    extractfmt = 'excel'
                else:
                    extractfmt = 'json'

        if extractfmt != 'json':
            headers: list[Header] = []
            for name, field in self.root.fields.items():
                if isinstance(field, Field):
                    header = Header(name, fmt=field.fmt, multiply=field.multiply)
                    headers.append(header)
                elif isinstance(field, FieldGroup):
                    if field.table:
                        if isinstance(field.table, FieldGroup):
                            logger.warning(f"Extraction {self.name}: ignore field {field.fullkey} (table cannot be a fieldgroup)")  # otherwise there would not be a matching key in the data dict
                        elif field.table.attrs is None: # null
                            pass # ignore
                        else:                            
                            header = Header(name, fmt=field.table.fmt, multiply=field.table.multiply)
                            headers.append(header)
                    else:
                        header = Header(name)
                        headers.append(header)
                else:
                    raise TypeError(f'field: {field}')
                
            if (extractfmt == 'tabulate' or (not extractfmt and (out == sys.stdout or out == sys.stderr))) and self.tabulate:
                headers = [header for header in headers if header.name in self.tabulate]

        with OutFile(out, title=title) if extractfmt == 'json' else OutTable(out, headers=headers, title=title, tablefmt=extractfmt) as o:
            if not isinstance(o, OutTable):
                if top != 1:
                    o.file.write('[')

            for i, obj in enumerate(self.get_objs(**options)):
                name, ignore_reason = self.get_obj_name_or_ignore_reason(obj)
                if ignore_reason:
                    logger.warning(f"ignore {name}: {ignore_reason}")
                    continue
                
                logger.info(f"analyze {name}")

                data = self.finalize_extracted_obj(self.extract_field(obj, self.root, extractfmt=extractfmt))
                if isinstance(o, OutTable):
                    if o.tablefmt == 'tabulate' and self.tabulate:
                        data = {key: value for key, value in data.items() if key in self.tabulate}
                    o.append(data)
                else:
                    if i > 0:
                        o.file.write(',')
                    _json.dump(data, o.file, ensure_ascii=False, indent=4, cls=ExtendedJSONEncoder)
                    o.file.flush()

                if top is not None and i == top - 1:
                    break

            if not isinstance(o, OutTable):
                if top != 1:
                    o.file.write(']')


    def get_objs(self, **options):
        raise NotImplementedError()


    def finalize_extracted_obj(self, obj):
        return obj
    

    def get_obj_name_or_ignore_reason(self, obj):
        try:
            return self.get_obj_name(obj), None
        except Exception as err:
            return str(obj), f"{type(err).__name__}: {str(err)}"


    def extract_field(self, obj, field: Field|FieldGroup, *, extractfmt: Literal['json', 'csv', 'tabulate']):
        if isinstance(field, FieldGroup):
            if field.root:
                obj = self.extract_obj_attr(obj, field.root.attrs)
                if extractfmt == 'json':
                    obj = field.root.convert(obj)

            if extractfmt != 'json' and field.table:
                return self.extract_field(obj, field.table, extractfmt=extractfmt)
            
            if not field.fields:
                # e.g. only _root and _table.
                return obj

            if isinstance(obj, list):
                result = []
                for elem in obj:
                    elem_result = {}
                    for subname, subfield in field.fields.items():
                        elem_result[subname] = self.extract_field(elem, subfield, extractfmt=extractfmt)
                    result.append(elem_result)
            else:
                result = {}
                for subname, subfield in field.fields.items():                    
                    result[subname] = self.extract_field(obj, subfield, extractfmt=extractfmt)

            return result

        else:
            value = self.extract_obj_attr(obj, field.attrs)
            if extractfmt == 'json':
                value = field.convert(value)
            return value


    def extract_obj_attr(self, obj, attrs: list[str]|None, *, vars_lookup: bool = True):
        if not attrs:
            return None
    
        attr = attrs[0]
        remaining = attrs[1:]

        if obj is None:
            return None
        elif isinstance(obj, list):
            if m := re.match(r'^([^\(]+)\((.*)\)$', attr):
                method = getattr(self, m[1])
                params_str = m[2].split()
                params = m[2].split(',') if params_str else []
                result = method(obj, *params)
            else:
                result = [self.extract_obj_attr(sub, attrs) for sub in obj]
        elif m := re.match(r'^([^\(]+)\((.*)\)$', attr):
            method = getattr(self, m[1])
            params_str = m[2].split()
            params = m[2].split(',') if params_str else []
            result = method(obj, *params)
        elif vars_lookup and attr in self.vars:
            if not attr in self._resolved_vars:
                self._resolved_vars[attr] = {}
            if not obj in self._resolved_vars[attr]:
                var_field = self.vars[attr]
                self._resolved_vars[attr][obj] = self.extract_obj_attr(obj, var_field.attrs, vars_lookup=False)
            result = self._resolved_vars[attr][obj]
        else:
            result = self.get_obj_attr(obj, attr)

        if remaining:
            if result is None:
                return None
            else:
                return self.extract_obj_attr(result, remaining, vars_lookup=False)
        else:
            return result


    def get_obj_attr(self, obj, attr: str):
        """
        Default function for `extract_obj_attr`.
        """
        return obj.get(attr) if isinstance(obj, dict) else getattr(obj, attr)
    
    def filter(self, obj, *params: str):
        def filter_func(x):
            for param in params:
                if not hasattr(x, param):
                    return False
            return True
        return list(filter(filter_func, obj))
    
    def sum(self, obj, *params: str):
        if len(params) != 1:
            raise ValueError(f"sum() must have exactly one param")
        return sum(getattr(x, params[0]) for x in obj)


class FieldGroup:
    def __init__(self, fullkey: str):
        self.fullkey = fullkey
        self.root: Field = None
        self.table: Field = None
        self.fields = {}


class Field(Header):
    def __init__(self, fullkey: str, attr: str|None):
        super().__init__(name=fullkey)
        self.fullkey = fullkey
        self.attrs = self._parse_attr(attr)


    def _parse_attr(self, text):
        if text is None:
            return None
        
        parts = []

        next_part = ''
        escaped = False
        for c in text:
            if escaped:
                if c == "'":
                    escaped = None
                    parts.append(next_part)
                    next_part = ''
                else:
                    next_part += c
            
            else:
                if c == "'":
                    escaped = True
                elif c == ".":
                    parts.append(next_part)
                    next_part = ''
                else:
                    next_part += c

        if next_part:
            parts.append(next_part)
        return parts


T_Extraction = TypeVar('T_Extraction', bound=Extraction)

def get_extractions(prog_module: ModuleType|Path|str, *, cls: type[T_Extraction] = Extraction, **cls_kwargs) -> dict[str,T_Extraction]:
    definition_files_by_name: dict[str,Path] = {}
    for parent in get_config_paths(prog_module, 'extractions', if_exist=True):
        for definition_file in parent.glob('*.yml'):
            name = definition_file.stem
            if name in ['list']:
                logger.warning(f"Ignored extraction with reserved name \"{name}\": {definition_file}")
            else:
                definition_files_by_name[name] = definition_file

    extractions = {}
    for name, definition_file in definition_files_by_name.items():
        try:
            extractions[name] = cls(name, definition_file, **cls_kwargs)
        except Exception as err:
            logger.warning(f"Ignored extraction \"{name}\": [{type(err).__name__}] {err} ({definition_file})")

    return extractions
