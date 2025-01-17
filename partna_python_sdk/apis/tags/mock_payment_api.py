# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from partna_python_sdk.paths.v1_mock_payment.post import RequestSubmission
from partna_python_sdk.apis.tags.mock_payment_api_raw import MockPaymentApiRaw


class MockPaymentApi(
    RequestSubmission,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MockPaymentApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MockPaymentApiRaw(api_client)
