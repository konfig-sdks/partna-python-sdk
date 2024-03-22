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


class TransactionsGetMerchantTransactionSummaryResponseData(BaseModel):
    # Total count of paid vouchers
    total_paid: typing.Optional[int] = Field(None, alias='totalPaid')

    # Total count of redeemed vouchers
    total_redeemed: typing.Optional[int] = Field(None, alias='totalRedeemed')

    # Total count of unpaid vouchers
    total_unpaid: typing.Optional[int] = Field(None, alias='totalUnpaid')

    # Total count of unredeemed vouchers
    total_unredeemed: typing.Optional[int] = Field(None, alias='totalUnredeemed')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )