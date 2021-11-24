import requests
import json
import time
import datetime 
import threading

authorization_string = 'token 26ud7j6qh471oabu:1O9uXoMgOLg39ptK7JbQxRcRzRjGnlE7'

def get_time():
    nanos = time.time_ns()
    secs = nanos / 1e9
    dt = datetime.datetime.fromtimestamp(secs)
    dt.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%f')

def place_order(data):
    print(threading.currentThread().getName())
    while True:
      # if True:
        if get_time().split('T')[1].split('.')[0]=='09:00:00':
            
            url = f'https://api.kite.trade/orders/regular'
            resp = requests.post(url, data = data,headers={'X-Kite-Version': '3','Authorization':authorization_string})
            parsed_response = json.loads(resp.content.decode("UTF-8"))

            print(parsed_response)

            print('ended')

            nanos = time.time_ns()
            secs = nanos / 1e9
            dt = datetime.datetime.fromtimestamp(secs)
            print(dt)
            break
    return



orders = [
  {
    'tradingsymbol':'IMFA',
    'exchange':'BSE',
    'transaction_type':'BUY',
    'order_type':'LIMIT',
    'quantity':200,
    'product':'CNC',
    'validity':'DAY',
    'price':754.3
},
{
    'tradingsymbol':'IMFA',
    'exchange':'NSE',
    'transaction_type':'BUY',
    'order_type':'LIMIT',
    'quantity':100,
    'product':'CNC',
    'validity':'DAY',
    'price':754
},

]

#  {
#     'tradingsymbol':'MEERA',
#     'exchange':'BSE',
#     'transaction_type':'SELL',
#     'order_type':'LIMIT',
#     'quantity':1141,
#     'product':'CNC',
#     'validity':'DAY',
#     'price':87
# },
# {
#     'tradingsymbol':'ZEAL',
#     'exchange':'BSE',
#     'transaction_type':'SELL',
#     'order_type':'LIMIT',
#     'quantity':1000,
#     'product':'CNC',
#     'validity':'DAY',
#     'price':84
# },
# {
#     'tradingsymbol':'JMCPROJECT',
#     'exchange':'NSE',
#     'transaction_type':'SELL',
#     'order_type':'LIMIT',
#     'quantity':1000,
#     'product':'CNC',
#     'validity':'DAY',
#     'price':115.7
# }

threads = [threading.Thread(name='t',target=place_order,args=(order,)) for order in orders ]

for thread in threads:
    thread.start()

