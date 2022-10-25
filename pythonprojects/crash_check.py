import efinance as ef
from datetime import datetime
import configparser
import json
import yfinance as yf

crashdate = datetime.today()


def statuscheck(ticker):
    msft = yf.Ticker(ticker)
    yesterday = msft.info['regularMarketPreviousClose']
    today = msft.info['regularMarketPrice']
    return (today - yesterday)/yesterday
print(statuscheck('^IXIC'))
# update the config.ini file everyday
config = configparser.ConfigParser()

config['AMOUNT'] = {
    'stock_amount' : 200,
    'budget' : 20000
}


config['PRICE'] = {
    'preHigh' : 174.55,
    'hisHigh' : 182.01
}

config['CRASH'] = {
    'crash' : 'y',
    'crashdate' : '2022-10-14',
    'resetdate' : '2022-11-17'
}

with  open('config.ini', 'w') as configfile:
    config.write(configfile)

print('The config.ini file is generated...')