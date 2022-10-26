import efinance as ef
from datetime import datetime
import configparser
import json
import yfinance as yf

crashdate = datetime.today()
crash_check = ''
# get the NASDAQ realtime index and calculate the movement percentage
def statuscheck(ticker):
    msft = yf.Ticker(ticker)
    yesterday = msft.info['regularMarketPreviousClose']
    print(yesterday)
    today = msft.info['regularMarketPrice']
    print(today)
    return (today - yesterday)/yesterday

# print(statuscheck('^IXIC'))

nasdaq_rate = statuscheck('^IXIC')
if nasdaq_rate <= -0.03:
    crash_check = 'y'
else:
    crash_check = 'n'
print(nasdaq_rate)
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
    'crash' : crash_check,
    'crashdate' : '2022-10-14',
    'resetdate' : '2022-11-15'
}

with  open('config.ini', 'w') as configfile:
    config.write(configfile)

print('The config.ini file is generated...')