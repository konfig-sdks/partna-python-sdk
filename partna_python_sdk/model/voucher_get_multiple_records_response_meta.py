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


class VoucherGetMultipleRecordsResponseMeta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            nextPage = schemas.StrSchema
            prevPage = schemas.StrSchema
            __annotations__ = {
                "nextPage": nextPage,
                "prevPage": prevPage,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPage"]) -> MetaOapg.properties.nextPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prevPage"]) -> MetaOapg.properties.prevPage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nextPage", "prevPage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPage"]) -> typing.Union[MetaOapg.properties.nextPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prevPage"]) -> typing.Union[MetaOapg.properties.prevPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nextPage", "prevPage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        nextPage: typing.Union[MetaOapg.properties.nextPage, str, schemas.Unset] = schemas.unset,
        prevPage: typing.Union[MetaOapg.properties.prevPage, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VoucherGetMultipleRecordsResponseMeta':
        return super().__new__(
            cls,
            *args,
            nextPage=nextPage,
            prevPage=prevPage,
            _configuration=_configuration,
            **kwargs,
        )
