import requests

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "123",
    "content-type": "application/json",
    "Host": "p2p.binance.com",
    "Origin": "https://p2p.binance.com",
    "Pragma": "no-cache",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

class getBinance:
  
  def buy():
    data = {
      "asset": "USDT",
      "fiat": "RUB",
      "merchantCheck": False,
      "page": 1,
      "payTypes": [],
      "publisherType": None,
      "rows": 10,
      "tradeType": "BUY"
    }
    r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data).json()
    
    userNo = r['data'][0]['advertiser']['userNo']
    
    return ({
      "maxLimit": r['data'][0]['adv']['maxSingleTransAmount'],
      "minLimit": r['data'][0]['adv']['minSingleTransQuantity'],
      "quantity": r['data'][0]['adv']['tradableQuantity'],
      "userName": r['data'][0]['advertiser']['nickName'],
      "price": r['data'][0]['adv']['price'],
      "link": f'https://p2p.binance.com/ru/advertiserDetail?advertiserNo={userNo}'
    })
    
  def sell():
    data = {
      "asset": "USDT",
      "fiat": "RUB",
      "merchantCheck": False,
      "page": 1,
      "payTypes": [],
      "publisherType": None,
      "rows": 10,
      "tradeType": "SELL"
    }
    r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data).json()
    
    userNo = r['data'][0]['advertiser']['userNo']
    
    return ({
      "maxLimit": r['data'][0]['adv']['maxSingleTransAmount'],
      "minLimit": r['data'][0]['adv']['minSingleTransQuantity'],
      "quantity": r['data'][0]['adv']['tradableQuantity'],
      "userName": r['data'][0]['advertiser']['nickName'],
      "price": r['data'][0]['adv']['price'],
      "link": f'https://p2p.binance.com/ru/advertiserDetail?advertiserNo={userNo}'
    })
  