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

from partna_python_sdk.type.balance_get_account_balance200_response_data import BalanceGetAccountBalance200ResponseData

class RequiredBalanceGetAccountBalance200Response(TypedDict):
    pass

class OptionalBalanceGetAccountBalance200Response(TypedDict, total=False):
    data: BalanceGetAccountBalance200ResponseData

    message: str

    success: bool

class BalanceGetAccountBalance200Response(RequiredBalanceGetAccountBalance200Response, OptionalBalanceGetAccountBalance200Response):
    pass