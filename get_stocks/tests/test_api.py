from get_stocks.alphaAPI import alpha_api_call, ALPHA_Exception
from django.test import TestCase
from unittest.mock import patch, Mock
import sys
from os import path
import requests


class TestAlphaAPICall(TestCase):

    def test_get_stock_data_not_found():
        with self.assertRaises(ALPHA_Exception) as ex_context:
            response = alpha_api_call('asdef', '5min')
            self.assertEqual('Error: ', str(ex_context.exception))


    def test_get_stock_with_no_API_KEY():

        with path.dict('os.environ', {'ALPHA_API_KEY': ''}):
            with self.assertRaises(ALPHA_Exception) as ex_context:
                response = alpha_api_call('AAPL', '5min')

            self.assertEqual('Invalid API key: ', str(ex_context.exception))








