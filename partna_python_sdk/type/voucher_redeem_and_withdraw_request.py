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


class RequiredVoucherRedeemAndWithdrawRequest(TypedDict):
    # Must be provided along with newtwork. The crypto wallet address on the provided network, to which crypto equivalent will be sent
    cryptoAddress: str

    # Cryptocurrency to send to the provided wallet details
    currency: str

    # Email that was used to create the voucher
    email: str

    # Supported crypto network
    network: str

    # Voucher code to be redeemed
    voucherCode: str

class OptionalVoucherRedeemAndWithdrawRequest(TypedDict, total=False):
    # In USD (optional) with a precision of 2 decimal places (max). Can be supplied if the merchant want to withdraw a portion of the voucher amount into their Ventogram balance. This must be a fraction or all of voucher value (ie received amount - voucher fee)
    merchantFee: str

    # This is a Ventogram-signed rate key. This will be returned in response if the signed rate was used for conversion.
    rateKey: str

class VoucherRedeemAndWithdrawRequest(RequiredVoucherRedeemAndWithdrawRequest, OptionalVoucherRedeemAndWithdrawRequest):
    pass
