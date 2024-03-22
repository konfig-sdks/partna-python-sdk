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


class BalanceWithdrawFundsRequest(BaseModel):
    # The account name. This is the name of the account holder.
    account_name: str = Field(alias='accountName')

    # The account number of the user's bank account.
    account_number: str = Field(alias='accountNumber')

    # The amount to be withdrawn.
    amount: str = Field(alias='amount')

    # The bank name. e.g. \"Access Bank\".
    bank: str = Field(alias='bank')

    # The bank code. e.g. \"044\".
    bank_code: str = Field(alias='bankCode')

    # The currency of the withdrawal.
    currency: str = Field(alias='currency')

    # The type of OTP to be used.
    otp_type: Literal["otp", "totp"] = Field(alias='otpType')

    # The token to be used for OTP.
    token: typing.Optional[str] = Field(None, alias='token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
