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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class BalanceTransferFundsResponseData(BaseModel):
    amount: typing.Optional[str] = Field(None, alias='amount')

    date: typing.Optional[date] = Field(None, alias='date')

    from_currency: typing.Optional[Literal["NGN", "USD"]] = Field(None, alias='fromCurrency')

    receive_amount: typing.Optional[str] = Field(None, alias='receiveAmount')

    sender: typing.Optional[str] = Field(None, alias='sender')

    sender_prevbalance: typing.Optional[str] = Field(None, alias='senderPrevbalance')

    status: typing.Optional[Literal["fullfiled", "processing", "failed"]] = Field(None, alias='status')

    to_currency: typing.Optional[Literal["NGN", "USD"]] = Field(None, alias='toCurrency')

    transaction_id: typing.Optional[str] = Field(None, alias='transactionId')

    username: typing.Optional[str] = Field(None, alias='username')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
