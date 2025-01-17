# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from partna_python_sdk.paths.v1_vouchers.post import CreatePaymentRaw
from partna_python_sdk.paths.v1_voucher_get_many.get import GetMultipleRecordsRaw
from partna_python_sdk.paths.v1_vouchers.get import GetRecordRaw
from partna_python_sdk.paths.v1_voucher.patch import RedeemAndWithdrawRaw
from partna_python_sdk.paths.v1_vouchers.patch import RedeemExistingUnusedRaw


class VoucherApiRaw(
    CreatePaymentRaw,
    GetMultipleRecordsRaw,
    GetRecordRaw,
    RedeemAndWithdrawRaw,
    RedeemExistingUnusedRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
