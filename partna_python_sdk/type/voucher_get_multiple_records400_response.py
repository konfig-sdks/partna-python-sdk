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

from partna_python_sdk.type.voucher_get_multiple_records400_response_errors import VoucherGetMultipleRecords400ResponseErrors

class RequiredVoucherGetMultipleRecords400Response(TypedDict):
    pass

class OptionalVoucherGetMultipleRecords400Response(TypedDict, total=False):
    errors: VoucherGetMultipleRecords400ResponseErrors

    message: str

    success: bool

class VoucherGetMultipleRecords400Response(RequiredVoucherGetMultipleRecords400Response, OptionalVoucherGetMultipleRecords400Response):
    pass
