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

from partna_python_sdk.type.voucher_fee_get_fee_response_data import VoucherFeeGetFeeResponseData

class RequiredVoucherFeeGetFeeResponse(TypedDict):
    pass

class OptionalVoucherFeeGetFeeResponse(TypedDict, total=False):
    data: VoucherFeeGetFeeResponseData

    message: str

    success: bool

class VoucherFeeGetFeeResponse(RequiredVoucherFeeGetFeeResponse, OptionalVoucherFeeGetFeeResponse):
    pass
