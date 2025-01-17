# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from partna_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from partna_python_sdk.api_response import AsyncGeneratorResponse
from partna_python_sdk import api_client, exceptions
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

from partna_python_sdk.model.transaction_get_user_transactions_response import TransactionGetUserTransactionsResponse as TransactionGetUserTransactionsResponseSchema

from partna_python_sdk.type.transaction_get_user_transactions_response import TransactionGetUserTransactionsResponse

from ...api_client import Dictionary
from partna_python_sdk.pydantic.transaction_get_user_transactions_response import TransactionGetUserTransactionsResponse as TransactionGetUserTransactionsResponsePydantic

# Query params


class CurrencySchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def NGN(cls):
        return cls("NGN")
    
    @schemas.classproperty
    def USD(cls):
        return cls("USD")


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DEPOSIT(cls):
        return cls("deposit")
    
    @schemas.classproperty
    def WITHDRAWAL(cls):
        return cls("withdrawal")
    
    @schemas.classproperty
    def SENT(cls):
        return cls("sent")
    
    @schemas.classproperty
    def TRANSFER(cls):
        return cls("transfer")
    
    @schemas.classproperty
    def INTERNAL_TRANSFER(cls):
        return cls("internalTransfer")
    
    @schemas.classproperty
    def CONVERSION(cls):
        return cls("conversion")
PageSchema = schemas.NumberSchema
LimitSchema = schemas.NumberSchema


class DurationSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DAY(cls):
        return cls("one day")
    
    @schemas.classproperty
    def WEEK(cls):
        return cls("one week")
    
    @schemas.classproperty
    def MONTH(cls):
        return cls("one month")
    
    @schemas.classproperty
    def YEAR(cls):
        return cls("one year")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'currency': typing.Union[CurrencySchema, str, ],
        'type': typing.Union[TypeSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, float, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, float, ],
        'duration': typing.Union[DurationSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_currency = api_client.QueryParameter(
    name="currency",
    style=api_client.ParameterStyle.FORM,
    schema=CurrencySchema,
    explode=True,
)
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_duration = api_client.QueryParameter(
    name="duration",
    style=api_client.ParameterStyle.FORM,
    schema=DurationSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = TransactionGetUserTransactionsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TransactionGetUserTransactionsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TransactionGetUserTransactionsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_user_transactions_mapped_args(
        self,
        currency: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if currency is not None:
            _query_params["currency"] = currency
        if type is not None:
            _query_params["type"] = type
        if page is not None:
            _query_params["page"] = page
        if limit is not None:
            _query_params["limit"] = limit
        if duration is not None:
            _query_params["duration"] = duration
        args.query = _query_params
        return args

    async def _aget_user_transactions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve user&#x27;s transaction records
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_currency,
            request_query_type,
            request_query_page,
            request_query_limit,
            request_query_duration,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/transaction',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_user_transactions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve user&#x27;s transaction records
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_currency,
            request_query_type,
            request_query_page,
            request_query_limit,
            request_query_duration,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/transaction',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetUserTransactionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_transactions(
        self,
        currency: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_transactions_mapped_args(
            currency=currency,
            type=type,
            page=page,
            limit=limit,
            duration=duration,
        )
        return await self._aget_user_transactions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_user_transactions(
        self,
        currency: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_transactions_mapped_args(
            currency=currency,
            type=type,
            page=page,
            limit=limit,
            duration=duration,
        )
        return self._get_user_transactions_oapg(
            query_params=args.query,
        )

class GetUserTransactions(BaseApi):

    async def aget_user_transactions(
        self,
        currency: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TransactionGetUserTransactionsResponsePydantic:
        raw_response = await self.raw.aget_user_transactions(
            currency=currency,
            type=type,
            page=page,
            limit=limit,
            duration=duration,
            **kwargs,
        )
        if validate:
            return TransactionGetUserTransactionsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TransactionGetUserTransactionsResponsePydantic, raw_response.body)
    
    
    def get_user_transactions(
        self,
        currency: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TransactionGetUserTransactionsResponsePydantic:
        raw_response = self.raw.get_user_transactions(
            currency=currency,
            type=type,
            page=page,
            limit=limit,
            duration=duration,
        )
        if validate:
            return TransactionGetUserTransactionsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TransactionGetUserTransactionsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        currency: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_transactions_mapped_args(
            currency=currency,
            type=type,
            page=page,
            limit=limit,
            duration=duration,
        )
        return await self._aget_user_transactions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        currency: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_transactions_mapped_args(
            currency=currency,
            type=type,
            page=page,
            limit=limit,
            duration=duration,
        )
        return self._get_user_transactions_oapg(
            query_params=args.query,
        )

