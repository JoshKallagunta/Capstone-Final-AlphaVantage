from get_stocks.alphaAPI import alpha_api_call
from django.test import TestCase
from unittest.mock import patch, Mock
import sys
from os import path
import requests


class TestAlphaAPICall(TestCase):

    #Tests if API does not find a ticker symbol 
    #Assert equal error message, goes not give 404 
    def test_get_stock_data_not_found(self):
        with self.assertRaises(Exception) as ex_context:
            response = alpha_api_call('asdef', '5min')
            self.assertEqual('Error: ', str(ex_context.exception))


    #Tests if the api has an invalid API Key 
    def test_get_stock_with_no_API_KEY(self):

        with patch.dict('os.environ', {'ALPHA_API_KEY': ''}):
            with self.assertRaises(Exception) as ex_context:
                response = alpha_api_call('AAPL', '5min')
                
            self.assertEquals('Invalid', str(ex_context.exception))








