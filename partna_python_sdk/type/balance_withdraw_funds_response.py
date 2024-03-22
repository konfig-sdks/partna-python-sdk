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


class RequiredBalanceWithdrawFundsResponse(TypedDict):
    pass

class OptionalBalanceWithdrawFundsResponse(TypedDict, total=False):
    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class BalanceWithdrawFundsResponse(RequiredBalanceWithdrawFundsResponse, OptionalBalanceWithdrawFundsResponse):
    pass
