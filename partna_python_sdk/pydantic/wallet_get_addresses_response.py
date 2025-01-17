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

from partna_python_sdk.pydantic.wallet_get_addresses_response_wallet import WalletGetAddressesResponseWallet

class WalletGetAddressesResponse(BaseModel):
    message: typing.Optional[str] = Field(None, alias='message')

    success: typing.Optional[bool] = Field(None, alias='success')

    wallet: typing.Optional[WalletGetAddressesResponseWallet] = Field(None, alias='wallet')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
