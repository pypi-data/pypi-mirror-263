"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from keymateapi import utils
from typing import List, Optional


@dataclasses.dataclass
class InternetsearchSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclasses.dataclass
class InternetsearchRequest:
    inputwindowwords: str = dataclasses.field(metadata={'query_param': { 'field_name': 'inputwindowwords', 'style': 'form', 'explode': True }})
    r"""Set it as '8000' first if responsetoolarge occurs reduce it to 1000."""
    q: str = dataclasses.field(metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    r"""Search query"""
    percentile: str = dataclasses.field(metadata={'query_param': { 'field_name': 'percentile', 'style': 'form', 'explode': True }})
    r"""Start it as '1', increase to '6' if ResponseTooLarge occurs, only reduce to '3' or '4' if user requests it."""
    numofpages: str = dataclasses.field(metadata={'query_param': { 'field_name': 'numofpages', 'style': 'form', 'explode': True }})
    r"""Start it as '6'. Retry the request by decreasing only this one if 'ResponseTooLarge' occurs. Should be between 1 and 10."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InternetsearchResponseResponseBody:
    r"""Error fetching search results"""
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    r"""Error message"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InternetsearchResults:
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the search result"""
    link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link'), 'exclude': lambda f: f is None }})
    r"""The URL of the search result"""
    summary: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary'), 'exclude': lambda f: f is None }})
    r"""A summary of the HTML content of the search result (available for the first five results)"""
    full_content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full_content'), 'exclude': lambda f: f is None }})
    r"""The entire HTML content of the search result (available for the first three results)"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InternetsearchResponseBody:
    r"""Successful operation"""
    results: Optional[List[InternetsearchResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    rules: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rules'), 'exclude': lambda f: f is None }})
    r"""The rules which recommend gpt to follow."""
    



@dataclasses.dataclass
class InternetsearchResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    two_hundred_application_json_object: Optional[InternetsearchResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    default_application_json_object: Optional[InternetsearchResponseResponseBody] = dataclasses.field(default=None)
    r"""Error fetching search results"""
    

