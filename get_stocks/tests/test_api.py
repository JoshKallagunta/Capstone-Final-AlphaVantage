from get_stocks.alphaAPI import alpha_api_call
from django.test import TestCase
from unittest.mock import patch, Mock
import sys
from os import path
import requests


class TestAlphaAPICall(TestCase):

    def test_get_stock_data_not_found(self):
        with self.assertRaises(Exception) as ex_context:
            response = alpha_api_call('asdef', '5min')
            self.assertEqual('Error: ', str(ex_context.exception))


    def test_get_stock_with_no_API_KEY(self):

        with patch.dict('os.environ', {'ALPHA_API_K': ''}):
            with self.assertRaises(Exception) as ex_context:
                response = alpha_api_call('AAPL', '5min')
                
            self.assertEquals('Invalid', str(ex_context.exception))








