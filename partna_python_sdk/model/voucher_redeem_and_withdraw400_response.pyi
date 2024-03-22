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


class VoucherRedeemAndWithdraw400Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def errors() -> typing.Type['VoucherRedeemAndWithdraw400ResponseErrors']:
                return VoucherRedeemAndWithdraw400ResponseErrors
            message = schemas.StrSchema
            
            
            class success(
                schemas.EnumBase,
                schemas.BoolSchema
            ):
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls(False)
            __annotations__ = {
                "errors": errors,
                "message": message,
                "success": success,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'VoucherRedeemAndWithdraw400ResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", "message", "success", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union['VoucherRedeemAndWithdraw400ResponseErrors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> typing.Union[MetaOapg.properties.success, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", "message", "success", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        errors: typing.Union['VoucherRedeemAndWithdraw400ResponseErrors', schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        success: typing.Union[MetaOapg.properties.success, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VoucherRedeemAndWithdraw400Response':
        return super().__new__(
            cls,
            *args,
            errors=errors,
            message=message,
            success=success,
            _configuration=_configuration,
            **kwargs,
        )

from partna_python_sdk.model.voucher_redeem_and_withdraw400_response_errors import VoucherRedeemAndWithdraw400ResponseErrors
