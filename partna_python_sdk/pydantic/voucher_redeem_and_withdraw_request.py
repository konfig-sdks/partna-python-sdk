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


class VoucherRedeemAndWithdrawRequest(BaseModel):
    # Must be provided along with newtwork. The crypto wallet address on the provided network, to which crypto equivalent will be sent
    crypto_address: str = Field(alias='cryptoAddress')

    # Cryptocurrency to send to the provided wallet details
    currency: Literal["USDC", "USDT"] = Field(alias='currency')

    # Email that was used to create the voucher
    email: str = Field(alias='email')

    # Supported crypto network
    network: str = Field(alias='network')

    # Voucher code to be redeemed
    voucher_code: str = Field(alias='voucherCode')

    # In USD (optional) with a precision of 2 decimal places (max). Can be supplied if the merchant want to withdraw a portion of the voucher amount into their Ventogram balance. This must be a fraction or all of voucher value (ie received amount - voucher fee)
    merchant_fee: typing.Optional[str] = Field(None, alias='merchantFee')

    # This is a Ventogram-signed rate key. This will be returned in response if the signed rate was used for conversion.
    rate_key: typing.Optional[str] = Field(None, alias='rateKey')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
