# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from partna_python_sdk.paths.v1_balance.get import GetAccountBalanceRaw
from partna_python_sdk.paths.balance.get import GetAccountBalance0Raw
from partna_python_sdk.paths.balance_transfer.post import TransferFundsRaw
from partna_python_sdk.paths.balance_withdraw.post import WithdrawFundsRaw


class BalanceApiRaw(
    GetAccountBalanceRaw,
    GetAccountBalance0Raw,
    TransferFundsRaw,
    WithdrawFundsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
