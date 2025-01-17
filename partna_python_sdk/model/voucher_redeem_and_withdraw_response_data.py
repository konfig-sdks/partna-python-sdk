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


class VoucherRedeemAndWithdrawResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            convertedVoucherFee = schemas.NumberSchema
            convertedVoucherFeeCurrency = schemas.StrSchema
            creditCurrency = schemas.StrSchema
            currentBalance = schemas.NumberSchema
            email = schemas.StrSchema
            
            
            class feeBearer(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "merchant": "MERCHANT",
                        "client": "CLIENT",
                    }
                
                @schemas.classproperty
                def MERCHANT(cls):
                    return cls("merchant")
                
                @schemas.classproperty
                def CLIENT(cls):
                    return cls("client")
            fromAmount = schemas.NumberSchema
            fromCurrency = schemas.StrSchema
            id = schemas.StrSchema
            merchant = schemas.StrSchema
            merchantFee = schemas.NumberSchema
            previousBalance = schemas.NumberSchema
            rate = schemas.NumberSchema
            reference = schemas.StrSchema
            toAccount = schemas.StrSchema
            toAmount = schemas.NumberSchema
            toCurrency = schemas.StrSchema
            voucherCode = schemas.StrSchema
            voucherFee = schemas.NumberSchema
            withdrawalFee = schemas.NumberSchema
            __annotations__ = {
                "convertedVoucherFee": convertedVoucherFee,
                "convertedVoucherFeeCurrency": convertedVoucherFeeCurrency,
                "creditCurrency": creditCurrency,
                "currentBalance": currentBalance,
                "email": email,
                "feeBearer": feeBearer,
                "fromAmount": fromAmount,
                "fromCurrency": fromCurrency,
                "id": id,
                "merchant": merchant,
                "merchantFee": merchantFee,
                "previousBalance": previousBalance,
                "rate": rate,
                "reference": reference,
                "toAccount": toAccount,
                "toAmount": toAmount,
                "toCurrency": toCurrency,
                "voucherCode": voucherCode,
                "voucherFee": voucherFee,
                "withdrawalFee": withdrawalFee,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["convertedVoucherFee"]) -> MetaOapg.properties.convertedVoucherFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["convertedVoucherFeeCurrency"]) -> MetaOapg.properties.convertedVoucherFeeCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creditCurrency"]) -> MetaOapg.properties.creditCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentBalance"]) -> MetaOapg.properties.currentBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeBearer"]) -> MetaOapg.properties.feeBearer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromAmount"]) -> MetaOapg.properties.fromAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromCurrency"]) -> MetaOapg.properties.fromCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant"]) -> MetaOapg.properties.merchant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantFee"]) -> MetaOapg.properties.merchantFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previousBalance"]) -> MetaOapg.properties.previousBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toAccount"]) -> MetaOapg.properties.toAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toAmount"]) -> MetaOapg.properties.toAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toCurrency"]) -> MetaOapg.properties.toCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voucherCode"]) -> MetaOapg.properties.voucherCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voucherFee"]) -> MetaOapg.properties.voucherFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withdrawalFee"]) -> MetaOapg.properties.withdrawalFee: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["convertedVoucherFee", "convertedVoucherFeeCurrency", "creditCurrency", "currentBalance", "email", "feeBearer", "fromAmount", "fromCurrency", "id", "merchant", "merchantFee", "previousBalance", "rate", "reference", "toAccount", "toAmount", "toCurrency", "voucherCode", "voucherFee", "withdrawalFee", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["convertedVoucherFee"]) -> typing.Union[MetaOapg.properties.convertedVoucherFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["convertedVoucherFeeCurrency"]) -> typing.Union[MetaOapg.properties.convertedVoucherFeeCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creditCurrency"]) -> typing.Union[MetaOapg.properties.creditCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentBalance"]) -> typing.Union[MetaOapg.properties.currentBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeBearer"]) -> typing.Union[MetaOapg.properties.feeBearer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromAmount"]) -> typing.Union[MetaOapg.properties.fromAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromCurrency"]) -> typing.Union[MetaOapg.properties.fromCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant"]) -> typing.Union[MetaOapg.properties.merchant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantFee"]) -> typing.Union[MetaOapg.properties.merchantFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previousBalance"]) -> typing.Union[MetaOapg.properties.previousBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> typing.Union[MetaOapg.properties.rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toAccount"]) -> typing.Union[MetaOapg.properties.toAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toAmount"]) -> typing.Union[MetaOapg.properties.toAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toCurrency"]) -> typing.Union[MetaOapg.properties.toCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voucherCode"]) -> typing.Union[MetaOapg.properties.voucherCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voucherFee"]) -> typing.Union[MetaOapg.properties.voucherFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withdrawalFee"]) -> typing.Union[MetaOapg.properties.withdrawalFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["convertedVoucherFee", "convertedVoucherFeeCurrency", "creditCurrency", "currentBalance", "email", "feeBearer", "fromAmount", "fromCurrency", "id", "merchant", "merchantFee", "previousBalance", "rate", "reference", "toAccount", "toAmount", "toCurrency", "voucherCode", "voucherFee", "withdrawalFee", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        convertedVoucherFee: typing.Union[MetaOapg.properties.convertedVoucherFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        convertedVoucherFeeCurrency: typing.Union[MetaOapg.properties.convertedVoucherFeeCurrency, str, schemas.Unset] = schemas.unset,
        creditCurrency: typing.Union[MetaOapg.properties.creditCurrency, str, schemas.Unset] = schemas.unset,
        currentBalance: typing.Union[MetaOapg.properties.currentBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        feeBearer: typing.Union[MetaOapg.properties.feeBearer, str, schemas.Unset] = schemas.unset,
        fromAmount: typing.Union[MetaOapg.properties.fromAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        fromCurrency: typing.Union[MetaOapg.properties.fromCurrency, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        merchant: typing.Union[MetaOapg.properties.merchant, str, schemas.Unset] = schemas.unset,
        merchantFee: typing.Union[MetaOapg.properties.merchantFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        previousBalance: typing.Union[MetaOapg.properties.previousBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        rate: typing.Union[MetaOapg.properties.rate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        reference: typing.Union[MetaOapg.properties.reference, str, schemas.Unset] = schemas.unset,
        toAccount: typing.Union[MetaOapg.properties.toAccount, str, schemas.Unset] = schemas.unset,
        toAmount: typing.Union[MetaOapg.properties.toAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        toCurrency: typing.Union[MetaOapg.properties.toCurrency, str, schemas.Unset] = schemas.unset,
        voucherCode: typing.Union[MetaOapg.properties.voucherCode, str, schemas.Unset] = schemas.unset,
        voucherFee: typing.Union[MetaOapg.properties.voucherFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        withdrawalFee: typing.Union[MetaOapg.properties.withdrawalFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VoucherRedeemAndWithdrawResponseData':
        return super().__new__(
            cls,
            *args,
            convertedVoucherFee=convertedVoucherFee,
            convertedVoucherFeeCurrency=convertedVoucherFeeCurrency,
            creditCurrency=creditCurrency,
            currentBalance=currentBalance,
            email=email,
            feeBearer=feeBearer,
            fromAmount=fromAmount,
            fromCurrency=fromCurrency,
            id=id,
            merchant=merchant,
            merchantFee=merchantFee,
            previousBalance=previousBalance,
            rate=rate,
            reference=reference,
            toAccount=toAccount,
            toAmount=toAmount,
            toCurrency=toCurrency,
            voucherCode=voucherCode,
            voucherFee=voucherFee,
            withdrawalFee=withdrawalFee,
            _configuration=_configuration,
            **kwargs,
        )
