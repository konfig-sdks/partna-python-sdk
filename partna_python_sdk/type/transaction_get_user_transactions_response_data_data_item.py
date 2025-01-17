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


class RequiredTransactionGetUserTransactionsResponseDataDataItem(TypedDict):
    pass

class OptionalTransactionGetUserTransactionsResponseDataDataItem(TypedDict, total=False):
    version: str

    amount: typing.Union[int, float]

    businessId: str

    createdAt: datetime

    currency: str

    date: str

    fee: typing.Union[int, float]

    fromAmount: typing.Union[int, float]

    fromCurrency: str

    isFromRegUser: bool

    prevBalance: typing.Union[int, float]

    sender: str

    senderPrevbalance: typing.Union[int, float]

    status: str

    transactionId: str

    type: str

    updatedAt: datetime

    username: str

class TransactionGetUserTransactionsResponseDataDataItem(RequiredTransactionGetUserTransactionsResponseDataDataItem, OptionalTransactionGetUserTransactionsResponseDataDataItem):
    pass
