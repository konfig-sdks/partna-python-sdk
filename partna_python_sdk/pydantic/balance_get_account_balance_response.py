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

from partna_python_sdk.pydantic.balance_get_account_balance_response_data import BalanceGetAccountBalanceResponseData

class BalanceGetAccountBalanceResponse(BaseModel):
    data: typing.Optional[BalanceGetAccountBalanceResponseData] = Field(None, alias='data')

    message: typing.Optional[str] = Field(None, alias='message')

    success: typing.Optional[Literal[True]] = Field(None, alias='success')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
