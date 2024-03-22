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


class TransactionGetUserTransactionSummaryResponseDataTxnDataItem(BaseModel):
    version: typing.Optional[str] = Field(None, alias='version')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    business_id: typing.Optional[str] = Field(None, alias='businessId')

    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    currency: typing.Optional[str] = Field(None, alias='currency')

    date: typing.Optional[str] = Field(None, alias='date')

    fee: typing.Optional[typing.Union[int, float]] = Field(None, alias='fee')

    from_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='fromAmount')

    from_currency: typing.Optional[str] = Field(None, alias='fromCurrency')

    is_from_reg_user: typing.Optional[bool] = Field(None, alias='isFromRegUser')

    prev_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='prevBalance')

    sender: typing.Optional[str] = Field(None, alias='sender')

    sender_prevbalance: typing.Optional[typing.Union[int, float]] = Field(None, alias='senderPrevbalance')

    status: typing.Optional[str] = Field(None, alias='status')

    transaction_id: typing.Optional[str] = Field(None, alias='transactionId')

    type: typing.Optional[str] = Field(None, alias='type')

    updated_at: typing.Optional[datetime] = Field(None, alias='updatedAt')

    username: typing.Optional[str] = Field(None, alias='username')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
