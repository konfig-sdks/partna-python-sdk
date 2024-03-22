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


class RequiredVoucherRedeemAndWithdrawResponseData(TypedDict):
    pass

class OptionalVoucherRedeemAndWithdrawResponseData(TypedDict, total=False):
    # Voucher fee in the outgoing currency
    convertedVoucherFee: typing.Union[int, float]

    # The same as toCurrency
    convertedVoucherFeeCurrency: str

    # Merchant's balance currency
    creditCurrency: str

    # Merchant's balance after redeeming voucher
    currentBalance: typing.Union[int, float]

    # Email that aws used to create the voucher
    email: str

    # The bearer of voucher fee
    feeBearer: str

    # Voucher payment amount.
    fromAmount: typing.Union[int, float]

    # voucher payment currency
    fromCurrency: str

    # Voucher ID
    id: str

    # username of the merchant that created the voucher
    merchant: str

    # This can be optionally provided by the merchant in the request if they want some of the received amount to be added to their Ventogram balance.
    merchantFee: typing.Union[int, float]

    # Merchant's balance before redeeming voucher
    previousBalance: typing.Union[int, float]

    # The exchange rate that was used for conversion (if applicable) at the time of redeeming the voucher. If there's no conversion, the value is 1.
    rate: typing.Union[int, float]

    # This is basically a unique id
    reference: str

    # The crypto wallet address to which asset was transferred
    toAccount: str

    # The amount that was sent to user wallet address.
    toAmount: typing.Union[int, float]

    # The currency that was sent to user wallet.
    toCurrency: str

    # Voucher code to be redeemed
    voucherCode: str

    # The fee associated with voucher in the payment currency. This will be deducted from merchant's balance if merchant is the fee bearer.
    voucherFee: typing.Union[int, float]

    # The processing fee for the crypto transfer that will be deducted from the merchant's account. Merchants must maintain a sufficient balance to utilize the redeem-and-withdraw endpoint.
    withdrawalFee: typing.Union[int, float]

class VoucherRedeemAndWithdrawResponseData(RequiredVoucherRedeemAndWithdrawResponseData, OptionalVoucherRedeemAndWithdrawResponseData):
    pass
