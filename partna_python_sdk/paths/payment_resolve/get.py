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

from partna_python_sdk.model.payment_resolve_overpaid_transaction_response import PaymentResolveOverpaidTransactionResponse as PaymentResolveOverpaidTransactionResponseSchema

from partna_python_sdk.type.payment_resolve_overpaid_transaction_response import PaymentResolveOverpaidTransactionResponse

from ...api_client import Dictionary
from partna_python_sdk.pydantic.payment_resolve_overpaid_transaction_response import PaymentResolveOverpaidTransactionResponse as PaymentResolveOverpaidTransactionResponsePydantic

from . import path

# Query params
IdSchema = schemas.StrSchema


class OptionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "refundexcess": "REFUNDEXCESS",
            "payall": "PAYALL",
        }
    
    @schemas.classproperty
    def REFUNDEXCESS(cls):
        return cls("refundexcess")
    
    @schemas.classproperty
    def PAYALL(cls):
        return cls("payall")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'id': typing.Union[IdSchema, str, ],
        'option': typing.Union[OptionSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    required=True,
    explode=True,
)
request_query_option = api_client.QueryParameter(
    name="option",
    style=api_client.ParameterStyle.FORM,
    schema=OptionSchema,
    required=True,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PaymentResolveOverpaidTransactionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaymentResolveOverpaidTransactionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaymentResolveOverpaidTransactionResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _resolve_overpaid_transaction_mapped_args(
        self,
        id: str,
        option: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if id is not None:
            _query_params["id"] = id
        if option is not None:
            _query_params["option"] = option
        args.query = _query_params
        return args

    async def _aresolve_overpaid_transaction_oapg(
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
        Resolve overpaid Transaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_id,
            request_query_option,
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
            path_template='/payment/resolve',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _resolve_overpaid_transaction_oapg(
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
        Resolve overpaid Transaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_id,
            request_query_option,
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
            path_template='/payment/resolve',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class ResolveOverpaidTransactionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aresolve_overpaid_transaction(
        self,
        id: str,
        option: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._resolve_overpaid_transaction_mapped_args(
            id=id,
            option=option,
        )
        return await self._aresolve_overpaid_transaction_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def resolve_overpaid_transaction(
        self,
        id: str,
        option: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._resolve_overpaid_transaction_mapped_args(
            id=id,
            option=option,
        )
        return self._resolve_overpaid_transaction_oapg(
            query_params=args.query,
        )

class ResolveOverpaidTransaction(BaseApi):

    async def aresolve_overpaid_transaction(
        self,
        id: str,
        option: str,
        validate: bool = False,
        **kwargs,
    ) -> PaymentResolveOverpaidTransactionResponsePydantic:
        raw_response = await self.raw.aresolve_overpaid_transaction(
            id=id,
            option=option,
            **kwargs,
        )
        if validate:
            return PaymentResolveOverpaidTransactionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentResolveOverpaidTransactionResponsePydantic, raw_response.body)
    
    
    def resolve_overpaid_transaction(
        self,
        id: str,
        option: str,
        validate: bool = False,
    ) -> PaymentResolveOverpaidTransactionResponsePydantic:
        raw_response = self.raw.resolve_overpaid_transaction(
            id=id,
            option=option,
        )
        if validate:
            return PaymentResolveOverpaidTransactionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentResolveOverpaidTransactionResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id: str,
        option: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._resolve_overpaid_transaction_mapped_args(
            id=id,
            option=option,
        )
        return await self._aresolve_overpaid_transaction_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        id: str,
        option: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._resolve_overpaid_transaction_mapped_args(
            id=id,
            option=option,
        )
        return self._resolve_overpaid_transaction_oapg(
            query_params=args.query,
        )
