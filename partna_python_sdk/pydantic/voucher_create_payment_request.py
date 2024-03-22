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


class VoucherCreatePaymentRequest(BaseModel):
    # Required voucher amount
    amount: int = Field(alias='amount')

    # Required voucher currency
    currency: Literal["NGN", "USD"] = Field(alias='currency')

    # User email
    email: str = Field(alias='email')

    # Fullname of the user creating voucher
    fullname: str = Field(alias='fullname')

    # This is a Ventogram-signed rate key. If provided when a voucher is created, the conversion will use the rate signed with this key if it is valid at the time of redeeming a voucher. Conversion will use the current rate if key has expired.
    rate_key: typing.Optional[str] = Field(None, alias='rateKey')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )