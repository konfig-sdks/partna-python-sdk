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

from partna_python_sdk.model.voucher_redeem_existing_unused_response import VoucherRedeemExistingUnusedResponse as VoucherRedeemExistingUnusedResponseSchema
from partna_python_sdk.model.voucher_redeem_existing_unused404_response import VoucherRedeemExistingUnused404Response as VoucherRedeemExistingUnused404ResponseSchema
from partna_python_sdk.model.voucher_redeem_existing_unused400_response import VoucherRedeemExistingUnused400Response as VoucherRedeemExistingUnused400ResponseSchema
from partna_python_sdk.model.voucher_redeem_existing_unused_request import VoucherRedeemExistingUnusedRequest as VoucherRedeemExistingUnusedRequestSchema

from partna_python_sdk.type.voucher_redeem_existing_unused_request import VoucherRedeemExistingUnusedRequest
from partna_python_sdk.type.voucher_redeem_existing_unused404_response import VoucherRedeemExistingUnused404Response
from partna_python_sdk.type.voucher_redeem_existing_unused_response import VoucherRedeemExistingUnusedResponse
from partna_python_sdk.type.voucher_redeem_existing_unused400_response import VoucherRedeemExistingUnused400Response

from ...api_client import Dictionary
from partna_python_sdk.pydantic.voucher_redeem_existing_unused_response import VoucherRedeemExistingUnusedResponse as VoucherRedeemExistingUnusedResponsePydantic
from partna_python_sdk.pydantic.voucher_redeem_existing_unused404_response import VoucherRedeemExistingUnused404Response as VoucherRedeemExistingUnused404ResponsePydantic
from partna_python_sdk.pydantic.voucher_redeem_existing_unused_request import VoucherRedeemExistingUnusedRequest as VoucherRedeemExistingUnusedRequestPydantic
from partna_python_sdk.pydantic.voucher_redeem_existing_unused400_response import VoucherRedeemExistingUnused400Response as VoucherRedeemExistingUnused400ResponsePydantic

# body param
SchemaForRequestBodyApplicationJson = VoucherRedeemExistingUnusedRequestSchema


request_body_voucher_redeem_existing_unused_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = VoucherRedeemExistingUnusedResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: VoucherRedeemExistingUnusedResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: VoucherRedeemExistingUnusedResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = VoucherRedeemExistingUnused400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: VoucherRedeemExistingUnused400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: VoucherRedeemExistingUnused400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = VoucherRedeemExistingUnused404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: VoucherRedeemExistingUnused404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: VoucherRedeemExistingUnused404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _redeem_existing_unused_mapped_args(
        self,
        email: str,
        voucher_code: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if email is not None:
            _body["email"] = email
        if voucher_code is not None:
            _body["voucherCode"] = voucher_code
        args.body = _body
        return args

    async def _aredeem_existing_unused_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Redeem existing unused voucher
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/vouchers',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_voucher_redeem_existing_unused_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _redeem_existing_unused_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Redeem existing unused voucher
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/vouchers',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_voucher_redeem_existing_unused_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class RedeemExistingUnusedRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aredeem_existing_unused(
        self,
        email: str,
        voucher_code: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._redeem_existing_unused_mapped_args(
            email=email,
            voucher_code=voucher_code,
        )
        return await self._aredeem_existing_unused_oapg(
            body=args.body,
            **kwargs,
        )
    
    def redeem_existing_unused(
        self,
        email: str,
        voucher_code: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._redeem_existing_unused_mapped_args(
            email=email,
            voucher_code=voucher_code,
        )
        return self._redeem_existing_unused_oapg(
            body=args.body,
        )

class RedeemExistingUnused(BaseApi):

    async def aredeem_existing_unused(
        self,
        email: str,
        voucher_code: str,
        validate: bool = False,
        **kwargs,
    ) -> VoucherRedeemExistingUnusedResponsePydantic:
        raw_response = await self.raw.aredeem_existing_unused(
            email=email,
            voucher_code=voucher_code,
            **kwargs,
        )
        if validate:
            return VoucherRedeemExistingUnusedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(VoucherRedeemExistingUnusedResponsePydantic, raw_response.body)
    
    
    def redeem_existing_unused(
        self,
        email: str,
        voucher_code: str,
        validate: bool = False,
    ) -> VoucherRedeemExistingUnusedResponsePydantic:
        raw_response = self.raw.redeem_existing_unused(
            email=email,
            voucher_code=voucher_code,
        )
        if validate:
            return VoucherRedeemExistingUnusedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(VoucherRedeemExistingUnusedResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        email: str,
        voucher_code: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._redeem_existing_unused_mapped_args(
            email=email,
            voucher_code=voucher_code,
        )
        return await self._aredeem_existing_unused_oapg(
            body=args.body,
            **kwargs,
        )
    
    def patch(
        self,
        email: str,
        voucher_code: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._redeem_existing_unused_mapped_args(
            email=email,
            voucher_code=voucher_code,
        )
        return self._redeem_existing_unused_oapg(
            body=args.body,
        )

