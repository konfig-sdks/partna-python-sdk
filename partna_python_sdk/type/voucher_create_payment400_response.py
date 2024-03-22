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

from partna_python_sdk.type.voucher_create_payment400_response_errors import VoucherCreatePayment400ResponseErrors

class RequiredVoucherCreatePayment400Response(TypedDict):
    pass

class OptionalVoucherCreatePayment400Response(TypedDict, total=False):
    errors: VoucherCreatePayment400ResponseErrors

    message: str

    success: bool

class VoucherCreatePayment400Response(RequiredVoucherCreatePayment400Response, OptionalVoucherCreatePayment400Response):
    pass
