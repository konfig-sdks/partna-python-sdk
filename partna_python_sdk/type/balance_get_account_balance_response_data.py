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


class RequiredBalanceGetAccountBalanceResponseData(TypedDict):
    pass

class OptionalBalanceGetAccountBalanceResponseData(TypedDict, total=False):
    # Merchant's balance amount
    amount: int

    # The currency passed by merchant
    currency: str

    # Merchant'susername
    merchant: str

    # Total count of voucher redeemption for a given merchant
    txnCount: int

class BalanceGetAccountBalanceResponseData(RequiredBalanceGetAccountBalanceResponseData, OptionalBalanceGetAccountBalanceResponseData):
    pass