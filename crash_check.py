import efinance as ef
import datetime
import configparser

crashdate = datetime.datetime.today()

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