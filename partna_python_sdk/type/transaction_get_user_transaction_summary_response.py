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

from partna_python_sdk.type.transaction_get_user_transaction_summary_response_data import TransactionGetUserTransactionSummaryResponseData

class RequiredTransactionGetUserTransactionSummaryResponse(TypedDict):
    pass

class OptionalTransactionGetUserTransactionSummaryResponse(TypedDict, total=False):
    data: TransactionGetUserTransactionSummaryResponseData

    message: str

    success: bool

class TransactionGetUserTransactionSummaryResponse(RequiredTransactionGetUserTransactionSummaryResponse, OptionalTransactionGetUserTransactionSummaryResponse):
    pass