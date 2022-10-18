import efinance as ef

#ef.stock.get_realtime_quotes()

preHigh = 174.55
hisHigh = 182.01
cPrice = float(input('Please input current price: '))

amount = 300
    
def horse_tick(hisHigh, cPrice):
    if cPrice >= hisHigh * (1-0.05):
        print('Sell 90% of the shares. To keep {0} shares. Set auto trade with price {1:.2f}'.format(amount * 0.1,\
            hisHigh * (1-0.05)))
    if hisHigh * (1-0.05) >= cPrice > hisHigh * (1-0.1):
        print('Keep 10% of the shares. To keep {0} shares'.format(amount * 0.1))
    if hisHigh * (1-0.1) >= cPrice > hisHigh * (1-0.15):
        print('Keep 20% of the shares. To keep {0} shares'.format(amount * 0.2))
    if hisHigh * (1-0.15) >= cPrice > hisHigh * (1-0.2):
        print('Keep 30% of the shares. To keep {0} shares'.format(amount * 0.3))    
    if hisHigh * (1-0.2) >= cPrice > hisHigh * (1-0.25):
        print('Keep 40% of the shares. To keep {0} shares'.format(amount * 0.4))  
    if hisHigh * (1-0.25) >= cPrice > hisHigh * (1-0.3):
        print('Keep 50% of the shares. To keep {0} shares'.format(amount * 0.5))  
    if hisHigh * (1-0.3) >= cPrice > hisHigh * (1-0.35):
        print('Keep 60% of the shares. To keep {0} shares'.format(amount * 0.6)) 
    if hisHigh * (1-0.35) >= cPrice > hisHigh * (1-0.4):
        print('Keep 70% of the shares. To keep {0} shares'.format(amount * 0.7)) 
    if hisHigh * (1-0.4) >= cPrice > hisHigh * (1-0.45):
        print('Keep 80% of the shares. To keep {0} shares'.format(amount * 0.8)) 
    if hisHigh * (1-0.45) >= cPrice > hisHigh * (1-0.5):
        print('Keep 90% of the shares. To keep {0} shares'.format(amount * 0.9)) 
    if hisHigh * (1-0.50) >= cPrice > hisHigh * (1-0.5):
        print('Keep 100% of the shares. To keep {0} shares'.format(amount * 1))       
    

def reblancing(preHigh, cPrice):
    if cPrice >= preHigh:
        preHigh = cPrice
        print('Now is new high price {0}, keep buying'.format(preHigh))
    if preHigh * (1-0.025) >= cPrice > preHigh * (1-0.05):
        print('keep 90% of the shares = {0} shares'.format(amount * 0.9))
    if preHigh * (1-0.05) >= cPrice > preHigh * (1-0.075):
        print('keep 80% of the shares = {0} shares'.format(amount * 0.8))
    if preHigh * (1-0.075) >= cPrice > preHigh * (1-0.1):
        print('keep 70% of the shares = {0} shares'.format(amount * 0.7))
    if preHigh * (1-0.1) >= cPrice > preHigh * (1-0.125):
        print('keep 60% of the shares = {0} shares'.format(amount * 0.6))
    if preHigh * (1-0.125) >= cPrice > preHigh * (1-0.15):
        print('keep 50% of the shares = {0} shares'.format(amount * 0.5))
    if preHigh * (1-0.15) >= cPrice > preHigh * (1-0.175):
        print('keep 40% of the shares = {0} shares'.format(amount * 0.4))
    if preHigh * (1-0.175) >= cPrice > preHigh * (1-0.2):
        print('keep 30% of the shares = {0} shares'.format(amount * 0.3))
    if preHigh * (1-0.2) >= cPrice > preHigh * (1-0.225):
        print('keep 20% of the shares = {0} shares'.format(amount * 0.2))
    if preHigh * (1-0.225) >= cPrice > preHigh * (1-0.25):
        print('keep 10% of the shares = {0} shares'.format(amount * 0.1))
    if preHigh * (1-0.25) >= cPrice:
        print('It is bare market, sell all!!!')

while True:

    crash = input('Is the NASDAQ dropped more than 3%?:(y or n)')

    if crash == 'y':
        horse_tick(hisHigh, cPrice)
        break
    if crash == 'n':
        reblancing(preHigh, cPrice)
        break
    else:
        print('Please input y or n.')


