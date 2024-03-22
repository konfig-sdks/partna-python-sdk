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


class RequiredApiKeyGenerateNewApiKeyResponseData(TypedDict):
    pass

class OptionalApiKeyGenerateNewApiKeyResponseData(TypedDict, total=False):
    expires: date

    key: str

class ApiKeyGenerateNewApiKeyResponseData(RequiredApiKeyGenerateNewApiKeyResponseData, OptionalApiKeyGenerateNewApiKeyResponseData):
    pass