# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from partna_python_sdk import schemas  # noqa: F401


class TransactionGetUserTransactionSummaryResponseDataTxnData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TransactionGetUserTransactionSummaryResponseDataTxnDataItem']:
            return TransactionGetUserTransactionSummaryResponseDataTxnDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TransactionGetUserTransactionSummaryResponseDataTxnDataItem'], typing.List['TransactionGetUserTransactionSummaryResponseDataTxnDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TransactionGetUserTransactionSummaryResponseDataTxnData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TransactionGetUserTransactionSummaryResponseDataTxnDataItem':
        return super().__getitem__(i)

from partna_python_sdk.model.transaction_get_user_transaction_summary_response_data_txn_data_item import TransactionGetUserTransactionSummaryResponseDataTxnDataItem
