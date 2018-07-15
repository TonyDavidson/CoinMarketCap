# Ian Annase
# Mastering The CoinMarketCap API with Python3

import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

convert = 'AUD'

global_url = 'https://api.coinmarketcap.com/v2/global/?convert=' + convert

request = requests.get(global_url)
results = request.json()
data = results['data']

global_cap = int(data['quotes'][convert]['total_market_cap'])
global_cap_string = '{:,}'.format(global_cap)



ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?convert='+convert+'&structure=array&sort='

    

request = requests.get(ticker_url)
results = request.json()
data = results['data']

    
    
       
quotes = data['quotes'][convert]['price']
print(quotes)

quot = data['quotes'][convert]['market_cap']
print(quot)

quo = data['quotes']['AUD']['price']
print(quo)
                     

                     
          
