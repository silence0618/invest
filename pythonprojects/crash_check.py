import efinance as ef
from datetime import datetime, timedelta
import configparser
import yfinance as yf

crashdate = datetime.today()
crash_check = ''

# get the NASDAQ realtime index and calculate the movement percentage
def statuscheck(ticker):
    price = yf.Ticker(ticker)
    yesterday = price.info['regularMarketPreviousClose']
    print(yesterday)
    today = price.info['regularMarketPrice']
    print(today)
    return (today - yesterday)/yesterday

# print(statuscheck('^IXIC'))

nasdaq_rate = statuscheck('^IXIC')


# update the nasdaq movement status
if nasdaq_rate <= -0.03:
    crash_check = 'y'
    crash_date = str(datetime.today())
    reset_date = crash_date + timedelta(days=31)
else:
    crash_check = 'n'
    date_time = '2022-10-14'

print(nasdaq_rate)

# update the hisHigh price


# update the config.ini file everyday
config = configparser.ConfigParser()

config['AMOUNT'] = {
    'stock_amount' : 250,
    'budget' : 20000
}


config['PRICE'] = {
    'preHigh' : 155.74,
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