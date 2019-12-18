import requests
import os
import logging
import json
from alpha_vantage.timeseries import TimeSeries 
from alpha_vantage.techindicators import TechIndicators
import pandas as pd 
from pprint import pprint

#
#log = logging.getLogger('__name__')

#def main():
def alpha_api_call(Symbol, Interval):

    api_key = '0B7Z2RG55NXJOCF3'

    ts = TimeSeries(key=api_key, output_format='pandas')

    stock_symbol = Symbol
    stock_interval = Interval

    print(stock_symbol)
    print(stock_interval)

    try: 
        data, meta_data = ts.get_intraday(symbol=stock_symbol,interval=stock_interval, outputsize='compact')

        ts_data = data
        print(ts_data)

        return ts_data

        # ts_data = pd.DataFrame(ts_data['Time Series (30min)'], orient= 'index').sort_index(axis=1)
        # ts_data = ts_data.rename(columns={ '1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. volume': 'Volume'})
        # ts_data = ts_data[[ 'Open', 'High', 'Low', 'Close', 'Volume']]

        # print(ts_data)
        # return ts_data


        #pprint(data.head(10))

        #json_dic = data.to_json()

        #print(json_dic)

        #return json_dic

    except Exception as e:
        print(e)
        #log.e('Error getting data from Alpha API', exc_info=e)


#if __name__ == '__main__':
    #main()
