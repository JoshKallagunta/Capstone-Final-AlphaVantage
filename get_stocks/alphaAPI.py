import requests
from django.shortcuts import redirect, render
import os
import logging
import json
from alpha_vantage.timeseries import TimeSeries 
from alpha_vantage.techindicators import TechIndicators
import pandas as pd 
from pprint import pprint
from get_stocks import views_search

class ALPHA_Exception(Exception):
    pass


def alpha_api_call(Symbol, Interval):

    api_key = os.environ.get('ALPHA_VANTAGE_KEY')

    ts = TimeSeries(key=api_key, output_format='pandas')

    #Parameters used for API call, getting from UI in forms 
    stock_symbol = Symbol
    stock_interval = Interval

    print(stock_symbol)
    print(stock_interval)

    #Try API call, using parameters, returns dataframe with the interday data 
    try: 
        data, meta_data = ts.get_intraday(symbol=stock_symbol,interval=stock_interval, outputsize='compact')

        return data

    except Exception as e:
        #Catches exceptions and logs it with a generic message + data about the error 
        print(e)
        raise ALPHA_Exception('Error:')
    
    except NameError as ne:
        #NameError raised when the API key is not correct 
        print(ne)
        raise ALPHA_Exception('Invalid API key: ')



