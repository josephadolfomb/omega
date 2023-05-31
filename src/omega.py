from binance.client import Client
import config

client = Client(config.apiKey, config.secretKey)
print("logged in")

#info = client.get_exchange_info()
#info = client.get_symbol_info('PEPEUSDT')
info = client.get_account()

#print(info)

#for i in info:
 #   print (i)

#timez = info['timezone']
#times = info['serverTime']
#print(times)

bal=info['balances']
#print (bal)
for b in bal:
    if float(b['free']) > 0 or float(b['locked']) > 0:
        print(b)
