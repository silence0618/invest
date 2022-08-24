

preHigh = 174.55
hisHigh = 182.01
cPrice = float(input('Please input current price: '))
amount = 200


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


reblancing(preHigh, cPrice)
