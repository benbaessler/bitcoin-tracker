import requests
import json

url = 'https://rest.coinapi.io/v1/assets'
headers = {'X-CoinAPI-Key': '573207D7-5AFE-4EF4-80F2-EAFF28134D8E'}
r = requests.get(url, headers = headers)
page = json.loads(r.text)

btc = page[0]
btc_value = round(btc['price_usd'], 2)

print(btc_value)
