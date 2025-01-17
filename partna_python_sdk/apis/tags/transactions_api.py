# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from partna_python_sdk.paths.v1_transactions_summary.get import GetMerchantTransactionSummary
from partna_python_sdk.apis.tags.transactions_api_raw import TransactionsApiRaw


class TransactionsApi(
    GetMerchantTransactionSummary,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TransactionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TransactionsApiRaw(api_client)
