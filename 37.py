import requests
 
def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': 'bitcoin,ethereum,litecoin', 'vs_currencies': 'usd'}
    response = requests.get(url, params=params)
    prices = response.json()
    return prices
 
crypto_prices = get_crypto_prices()
 
for coin, value in crypto_prices.items():
    print(f"{coin.capitalize()}: ${value['usd']}")
