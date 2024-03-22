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


class RatesGetCurrentRatesResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def YOUR_CURRENCY() -> typing.Type['RatesGetCurrentRatesResponseDataYourCurrency']:
                return RatesGetCurrentRatesResponseDataYourCurrency
            publicKey = schemas.StrSchema
            signature = schemas.StrSchema
            __annotations__ = {
                "YOUR_CURRENCY": YOUR_CURRENCY,
                "publicKey": publicKey,
                "signature": signature,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["YOUR_CURRENCY"]) -> 'RatesGetCurrentRatesResponseDataYourCurrency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicKey"]) -> MetaOapg.properties.publicKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature"]) -> MetaOapg.properties.signature: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["YOUR_CURRENCY", "publicKey", "signature", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["YOUR_CURRENCY"]) -> typing.Union['RatesGetCurrentRatesResponseDataYourCurrency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicKey"]) -> typing.Union[MetaOapg.properties.publicKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature"]) -> typing.Union[MetaOapg.properties.signature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["YOUR_CURRENCY", "publicKey", "signature", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        YOUR_CURRENCY: typing.Union['RatesGetCurrentRatesResponseDataYourCurrency', schemas.Unset] = schemas.unset,
        publicKey: typing.Union[MetaOapg.properties.publicKey, str, schemas.Unset] = schemas.unset,
        signature: typing.Union[MetaOapg.properties.signature, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RatesGetCurrentRatesResponseData':
        return super().__new__(
            cls,
            *args,
            YOUR_CURRENCY=YOUR_CURRENCY,
            publicKey=publicKey,
            signature=signature,
            _configuration=_configuration,
            **kwargs,
        )

from partna_python_sdk.model.rates_get_current_rates_response_data_your_currency import RatesGetCurrentRatesResponseDataYourCurrency
