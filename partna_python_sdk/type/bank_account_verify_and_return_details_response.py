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

from partna_python_sdk.type.bank_account_verify_and_return_details_response_data import BankAccountVerifyAndReturnDetailsResponseData

class RequiredBankAccountVerifyAndReturnDetailsResponse(TypedDict):
    pass

class OptionalBankAccountVerifyAndReturnDetailsResponse(TypedDict, total=False):
    data: BankAccountVerifyAndReturnDetailsResponseData

class BankAccountVerifyAndReturnDetailsResponse(RequiredBankAccountVerifyAndReturnDetailsResponse, OptionalBankAccountVerifyAndReturnDetailsResponse):
    pass
