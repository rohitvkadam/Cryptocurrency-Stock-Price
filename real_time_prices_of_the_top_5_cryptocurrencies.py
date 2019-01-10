import json
import requests

api_key = 'I0RJA713A3GG9BBE'

frm_cur = ['BTC', 'XRP', 'ETH', 'LTC', 'DOGE']
to_cur = ['USD']
for i in to_cur:
    for j in frm_cur:
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+j+'&to_currency='+i+'&apikey='+api_key
        ans = requests.get(url)
        result = json.loads(ans.text)
        calc = result['Real time Currency Exchange Rate']
        print(calc)
