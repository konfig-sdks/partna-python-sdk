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

from partna_python_sdk.type.transaction_get_user_transaction_summary_response_data_txn_data import TransactionGetUserTransactionSummaryResponseDataTxnData

class RequiredTransactionGetUserTransactionSummaryResponseDataTxn(TypedDict):
    pass

class OptionalTransactionGetUserTransactionSummaryResponseDataTxn(TypedDict, total=False):
    data: TransactionGetUserTransactionSummaryResponseDataTxnData

    page: typing.Union[int, float]

    pages: typing.Union[int, float]

    perPage: typing.Union[int, float]

    total: typing.Union[int, float]

class TransactionGetUserTransactionSummaryResponseDataTxn(RequiredTransactionGetUserTransactionSummaryResponseDataTxn, OptionalTransactionGetUserTransactionSummaryResponseDataTxn):
    pass
