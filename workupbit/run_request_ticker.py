
import requests


url_ticker = "https://api.upbit.com/v1/ticker"
querystring = {"markets":"KRW-BTC"}
response = requests.request("GET", url_ticker, params=querystring)

res_json = response.json()

print(res_json[0]['trade_price'])
