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


class VoucherGetMultipleRecordsResponseData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An array containing the retrieved voucher records, sorted in descending order by their creation date.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['VoucherGetMultipleRecordsResponseDataItem']:
            return VoucherGetMultipleRecordsResponseDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['VoucherGetMultipleRecordsResponseDataItem'], typing.List['VoucherGetMultipleRecordsResponseDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'VoucherGetMultipleRecordsResponseData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'VoucherGetMultipleRecordsResponseDataItem':
        return super().__getitem__(i)

from partna_python_sdk.model.voucher_get_multiple_records_response_data_item import VoucherGetMultipleRecordsResponseDataItem