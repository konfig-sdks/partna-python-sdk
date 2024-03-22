# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from partna_python_sdk.pydantic.currency_list_supported_currencies_response_data_incoming_currencies import CurrencyListSupportedCurrenciesResponseDataIncomingCurrencies
from partna_python_sdk.pydantic.currency_list_supported_currencies_response_data_outgoing_currencies import CurrencyListSupportedCurrenciesResponseDataOutgoingCurrencies

class CurrencyListSupportedCurrenciesResponseData(BaseModel):
    incoming_currencies: typing.Optional[CurrencyListSupportedCurrenciesResponseDataIncomingCurrencies] = Field(None, alias='incomingCurrencies')

    outgoing_currencies: typing.Optional[CurrencyListSupportedCurrenciesResponseDataOutgoingCurrencies] = Field(None, alias='outgoingCurrencies')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )