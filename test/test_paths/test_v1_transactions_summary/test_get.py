# coding: utf-8

"""
    Coinprofile business API

    Coinprofile business API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import partna_python_sdk
from partna_python_sdk.paths.v1_transactions_summary import get
from partna_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1TransactionsSummary(ApiTestMixin, unittest.TestCase):
    """
    V1TransactionsSummary unit test stubs
        Retrieve merchant transaction summary
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
