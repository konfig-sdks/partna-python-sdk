# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from partna_python_sdk.paths.bank_resolve.post import VerifyAndReturnDetails
from partna_python_sdk.apis.tags.bank_account_api_raw import BankAccountApiRaw


class BankAccountApi(
    VerifyAndReturnDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BankAccountApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BankAccountApiRaw(api_client)
