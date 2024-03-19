"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from keymateapi import utils
from typing import Any, List, Optional


@dataclasses.dataclass
class AcademicsearchdoiSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclasses.dataclass
class AcademicsearchdoiRequest:
    doi: str = dataclasses.field(metadata={'query_param': { 'field_name': 'doi', 'style': 'form', 'explode': True }})
    r"""The doi of the academic paper user wants to chat with or ground asisstant responses. Only provide DOI (find the DOI from user's input) if URL is given use /browseurl on it to find the DOI"""
    q: str = dataclasses.field(metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    r"""The question about the paper if user directs a question or query to you if they don't provide set it as NotExist"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AcademicsearchdoiMetadata:
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Your nearest neighbour response to the user related to your query"""
    



@dataclasses.dataclass
class AcademicsearchdoiSparseValues:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AcademicsearchdoiMatches:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""User's unique id with timestamp the data was inserted to long term memory."""
    metadata: Optional[AcademicsearchdoiMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    score: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score'), 'exclude': lambda f: f is None }})
    r"""How close was the results to your query"""
    sparse_values: Optional[AcademicsearchdoiSparseValues] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sparseValues'), 'exclude': lambda f: f is None }})
    values: Optional[List[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('values'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AcademicsearchdoiResponseBody:
    r"""Successful operation"""
    matches: Optional[List[AcademicsearchdoiMatches]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('matches'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class AcademicsearchdoiResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    object: Optional[AcademicsearchdoiResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    

