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


class RequiredVoucherRedeemExistingUnusedResponseData(TypedDict):
    pass

class OptionalVoucherRedeemExistingUnusedResponseData(TypedDict, total=False):
    # Voucher amount after fee deduction
    amount: typing.Union[int, float]

    # voucher payment currency
    currency: str

    # Merchant's balance after redeeming voucher
    currentBalance: typing.Union[int, float]

    # Email that aws used to create the voucher
    email: str

    # The fee associated with voucher
    fee: typing.Union[int, float]

    # The bearer of voucher fee
    feeBearer: str

    # The amount in the currency that was converted from when conversion was done. If there's no conversion, this is the same as toAmount.
    fromAmount: typing.Union[int, float]

    # The currency from which conversion was done. If there's no conversion, this is the same as toCurrency.
    fromCurrency: str

    # Voucher ID
    id: str

    # username of the merchant that created the voucher
    merchant: str

    # Merchant's balance before redeeming voucher
    previousBalance: typing.Union[int, float]

    # The exchange rate that was used for conversion when conversion was done. If there's no conversion, the value is 1.
    rate: typing.Union[int, float]

    # The amount in the currency that was converted to when conversion was done. If there's no conversion, this is the same as fromAmount.
    toAmount: typing.Union[int, float]

    # The currency to which conversion was done. If there's no conversion, this is the same as fromCurrency.
    toCurrency: str

    # Voucher code to be redeemed
    voucherCode: str

    # Waved fee (if available)
    wavedFee: typing.Union[int, float]

class VoucherRedeemExistingUnusedResponseData(RequiredVoucherRedeemExistingUnusedResponseData, OptionalVoucherRedeemExistingUnusedResponseData):
    pass
