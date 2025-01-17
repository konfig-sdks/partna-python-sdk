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

from partna_python_sdk.type.balance_get_account_balance200_response_data_balances import BalanceGetAccountBalance200ResponseDataBalances

class RequiredBalanceGetAccountBalance200ResponseData(TypedDict):
    pass

class OptionalBalanceGetAccountBalance200ResponseData(TypedDict, total=False):
    balances: BalanceGetAccountBalance200ResponseDataBalances

class BalanceGetAccountBalance200ResponseData(RequiredBalanceGetAccountBalance200ResponseData, OptionalBalanceGetAccountBalance200ResponseData):
    pass
