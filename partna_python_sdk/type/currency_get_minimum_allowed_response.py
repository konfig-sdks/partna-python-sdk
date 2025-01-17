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

from partna_python_sdk.type.currency_get_minimum_allowed_response_data import CurrencyGetMinimumAllowedResponseData

class RequiredCurrencyGetMinimumAllowedResponse(TypedDict):
    pass

class OptionalCurrencyGetMinimumAllowedResponse(TypedDict, total=False):
    data: CurrencyGetMinimumAllowedResponseData

class CurrencyGetMinimumAllowedResponse(RequiredCurrencyGetMinimumAllowedResponse, OptionalCurrencyGetMinimumAllowedResponse):
    pass
