# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from partna_python_sdk.paths.transaction_transaction_id.get import GetDetails
from partna_python_sdk.paths.transaction_summary.get import GetUserTransactionSummary
from partna_python_sdk.paths.transaction.get import GetUserTransactions
from partna_python_sdk.apis.tags.transaction_api_raw import TransactionApiRaw


class TransactionApi(
    GetDetails,
    GetUserTransactionSummary,
    GetUserTransactions,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TransactionApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TransactionApiRaw(api_client)