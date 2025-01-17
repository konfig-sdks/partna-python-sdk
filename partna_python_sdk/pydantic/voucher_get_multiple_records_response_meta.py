# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class VoucherGetMultipleRecordsResponseMeta(BaseModel):
    # Contanis the URL of the next page to be fetched relative on the URL parameters of the last paged fetched. This is null if there are no more records to fetch.
    next_page: typing.Optional[str] = Field(None, alias='nextPage')

    # Contanis the URL of the previous page that was fetched fetched relative on the URL parameters of the current paged
    prev_page: typing.Optional[str] = Field(None, alias='prevPage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
