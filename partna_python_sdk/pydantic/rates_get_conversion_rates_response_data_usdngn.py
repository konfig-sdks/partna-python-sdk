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


class RatesGetConversionRatesResponseDataUsdngn(BaseModel):
    # description text
    description: typing.Optional[str] = Field(None, alias='description')

    # Ventogram signed rate key
    rate_key: typing.Optional[str] = Field(None, alias='rateKey')

    # 1 USD is equal to 500 NGN in this example
    value: typing.Optional[int] = Field(None, alias='value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )