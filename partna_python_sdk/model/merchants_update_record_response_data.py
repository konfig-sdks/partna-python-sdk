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


class MerchantsUpdateRecordResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            callbackUrl = schemas.StrSchema
            
            
            class creditCurrency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NGN": "NGN",
                        "USD": "USD",
                    }
                
                @schemas.classproperty
                def NGN(cls):
                    return cls("NGN")
                
                @schemas.classproperty
                def USD(cls):
                    return cls("USD")
            feeBearer = schemas.StrSchema
            logo = schemas.StrSchema
            username = schemas.StrSchema
            __annotations__ = {
                "callbackUrl": callbackUrl,
                "creditCurrency": creditCurrency,
                "feeBearer": feeBearer,
                "logo": logo,
                "username": username,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callbackUrl"]) -> MetaOapg.properties.callbackUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creditCurrency"]) -> MetaOapg.properties.creditCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeBearer"]) -> MetaOapg.properties.feeBearer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["callbackUrl", "creditCurrency", "feeBearer", "logo", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callbackUrl"]) -> typing.Union[MetaOapg.properties.callbackUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creditCurrency"]) -> typing.Union[MetaOapg.properties.creditCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeBearer"]) -> typing.Union[MetaOapg.properties.feeBearer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["callbackUrl", "creditCurrency", "feeBearer", "logo", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        callbackUrl: typing.Union[MetaOapg.properties.callbackUrl, str, schemas.Unset] = schemas.unset,
        creditCurrency: typing.Union[MetaOapg.properties.creditCurrency, str, schemas.Unset] = schemas.unset,
        feeBearer: typing.Union[MetaOapg.properties.feeBearer, str, schemas.Unset] = schemas.unset,
        logo: typing.Union[MetaOapg.properties.logo, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MerchantsUpdateRecordResponseData':
        return super().__new__(
            cls,
            *args,
            callbackUrl=callbackUrl,
            creditCurrency=creditCurrency,
            feeBearer=feeBearer,
            logo=logo,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )
