import requests
import json
import time
import datetime 
import threading

authorization_string = 'token 26ud7j6qh471oabu:cTNOanbM4yZBZCkSzeFgYY8XCVTWP32X'

def get_time():
    nanos = time.time_ns()
    secs = nanos / 1e9
    dt = datetime.datetime.fromtimestamp(secs)
    dt.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%f')

def place_order(data):
    print(threading.currentThread().getName())
    while True:
       
        if get_time().split('T')[1].split('.')[0]=='01:06:00':
            # url = f'https://api.kite.trade/gtt/triggers'
            url = f'https://api.kite.trade/orders/regular'
            resp = requests.post(url, data = data,headers={'X-Kite-Version': '3','Authorization':authorization_string})
            parsed_response = json.loads(resp.content.decode("UTF-8"))

            print(parsed_response)

            while parsed_response['status'] == 'error':
                resp = requests.post(url, data = data,headers={'X-Kite-Version': '3','Authorization':authorization_string})
                parsed_response = json.loads(resp.content.decode("UTF-8"))
                print(parsed_response)
                parsed_response['status'] = parsed_response['status']

            print('ended')

            nanos = time.time_ns()
            secs = nanos / 1e9
            dt = datetime.datetime.fromtimestamp(secs)
            print(dt)
            break
    return

# orders = [{
#             'type': 'single',
#             'condition': '{"exchange":"NSE", "tradingsymbol":"INFY", "trigger_values":[702.0], "last_price": 798.0}',
#             'orders': '[{"exchange":"NSE", "tradingsymbol": "INFY", "transaction_type": "BUY", "quantity": 1, "order_type": "LIMIT","product": "CNC", "price": 702.5}]'
#             },{
#             'type': 'single',
#             'condition': '{"exchange":"NSE", "tradingsymbol":"BOMBWIR", "trigger_values":[702.0], "last_price": 798.0}',
#             'orders': '[{"exchange":"NSE", "tradingsymbol": "BOMBWIR", "transaction_type": "BUY", "quantity": 1, "order_type": "LIMIT","product": "CNC", "price": 702.5}]'
#             }]

orders = [{
    'tradingsymbol':'BOMBWIR',
    'exchange':'BSE',
    'transaction_type':'BUY',
    'order_type':'LIMIT',
    'quantity':1,
    'product':'CNC',
    'validity':'DAY',
    'price':11.83
},{
    'tradingsymbol':'BOMBWIR',
    'exchange':'BSE',
    'transaction_type':'BUY',
    'order_type':'LIMIT',
    'quantity':1,
    'product':'CNC',
    'validity':'DAY',
    'price':11.83
}]

threads = [threading.Thread(name='t',target=place_order,args=(order,)) for order in orders ]

for thread in threads:
    thread.start()

