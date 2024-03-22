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


class RequiredWalletGetSupportedConfigResponseData(TypedDict):
    pass

class OptionalWalletGetSupportedConfigResponseData(TypedDict, total=False):
    byCurrency: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    byNetwork: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class WalletGetSupportedConfigResponseData(RequiredWalletGetSupportedConfigResponseData, OptionalWalletGetSupportedConfigResponseData):
    pass