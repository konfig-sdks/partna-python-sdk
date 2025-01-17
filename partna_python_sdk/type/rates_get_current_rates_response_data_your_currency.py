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


class RequiredRatesGetCurrentRatesResponseDataYourCurrency(TypedDict):
    pass

class OptionalRatesGetCurrentRatesResponseDataYourCurrency(TypedDict, total=False):
    key: str

    rate: typing.Union[int, float]

class RatesGetCurrentRatesResponseDataYourCurrency(RequiredRatesGetCurrentRatesResponseDataYourCurrency, OptionalRatesGetCurrentRatesResponseDataYourCurrency):
    pass
