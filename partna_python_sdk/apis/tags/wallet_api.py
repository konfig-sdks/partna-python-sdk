# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from partna_python_sdk.paths.wallet_transfer.post import ExecuteTransfer
from partna_python_sdk.paths.wallet.get import GetAddresses
from partna_python_sdk.paths.wallet_supported_config.get import GetSupportedConfig
from partna_python_sdk.apis.tags.wallet_api_raw import WalletApiRaw


class WalletApi(
    ExecuteTransfer,
    GetAddresses,
    GetSupportedConfig,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WalletApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WalletApiRaw(api_client)