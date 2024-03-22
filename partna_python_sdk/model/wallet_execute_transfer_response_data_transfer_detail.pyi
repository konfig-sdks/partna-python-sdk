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


class WalletExecuteTransferResponseDataTransferDetail(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            address = schemas.StrSchema
            amount = schemas.NumberSchema
            date = schemas.StrSchema
            fromCurrency = schemas.StrSchema
            memo = schemas.StrSchema
            receiveAmount = schemas.NumberSchema
            sender = schemas.StrSchema
            status = schemas.StrSchema
            toCurrency = schemas.StrSchema
            transactionId = schemas.StrSchema
            type = schemas.StrSchema
            username = schemas.StrSchema
            __annotations__ = {
                "address": address,
                "amount": amount,
                "date": date,
                "fromCurrency": fromCurrency,
                "memo": memo,
                "receiveAmount": receiveAmount,
                "sender": sender,
                "status": status,
                "toCurrency": toCurrency,
                "transactionId": transactionId,
                "type": type,
                "username": username,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromCurrency"]) -> MetaOapg.properties.fromCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memo"]) -> MetaOapg.properties.memo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiveAmount"]) -> MetaOapg.properties.receiveAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender"]) -> MetaOapg.properties.sender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toCurrency"]) -> MetaOapg.properties.toCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionId"]) -> MetaOapg.properties.transactionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address", "amount", "date", "fromCurrency", "memo", "receiveAmount", "sender", "status", "toCurrency", "transactionId", "type", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromCurrency"]) -> typing.Union[MetaOapg.properties.fromCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memo"]) -> typing.Union[MetaOapg.properties.memo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiveAmount"]) -> typing.Union[MetaOapg.properties.receiveAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender"]) -> typing.Union[MetaOapg.properties.sender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toCurrency"]) -> typing.Union[MetaOapg.properties.toCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionId"]) -> typing.Union[MetaOapg.properties.transactionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address", "amount", "date", "fromCurrency", "memo", "receiveAmount", "sender", "status", "toCurrency", "transactionId", "type", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        fromCurrency: typing.Union[MetaOapg.properties.fromCurrency, str, schemas.Unset] = schemas.unset,
        memo: typing.Union[MetaOapg.properties.memo, str, schemas.Unset] = schemas.unset,
        receiveAmount: typing.Union[MetaOapg.properties.receiveAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sender: typing.Union[MetaOapg.properties.sender, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        toCurrency: typing.Union[MetaOapg.properties.toCurrency, str, schemas.Unset] = schemas.unset,
        transactionId: typing.Union[MetaOapg.properties.transactionId, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletExecuteTransferResponseDataTransferDetail':
        return super().__new__(
            cls,
            *args,
            address=address,
            amount=amount,
            date=date,
            fromCurrency=fromCurrency,
            memo=memo,
            receiveAmount=receiveAmount,
            sender=sender,
            status=status,
            toCurrency=toCurrency,
            transactionId=transactionId,
            type=type,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )
