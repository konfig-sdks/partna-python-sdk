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


class MerchantsUpdateRecordResponseData(BaseModel):
    callback_url: typing.Optional[str] = Field(None, alias='callbackUrl')

    credit_currency: typing.Optional[Literal["NGN", "USD"]] = Field(None, alias='creditCurrency')

    fee_bearer: typing.Optional[str] = Field(None, alias='feeBearer')

    logo: typing.Optional[str] = Field(None, alias='logo')

    username: typing.Optional[str] = Field(None, alias='username')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )