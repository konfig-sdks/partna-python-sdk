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


class RequiredVoucherCreatePaymentResponseData(TypedDict):
    pass

class OptionalVoucherCreatePaymentResponseData(TypedDict, total=False):
    # Voucher unique id
    id: str

class VoucherCreatePaymentResponseData(RequiredVoucherCreatePaymentResponseData, OptionalVoucherCreatePaymentResponseData):
    pass