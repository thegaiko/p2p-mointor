from pprint import pprint
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


def get_req(type, method):
    data = {
        "asset": "USDT",
        "fiat": "RUB",
        "merchantCheck": False,
        "page": 1,
        "payTypes": [method],
        "publisherType": None,
        "rows": 10,
        "tradeType": type
    }
    r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data).json()
    return r


class getBinance:

    def buy():
        r = get_req("BUY", "Tinkoff")
        qiwi = get_req("BUY", "QIWI")
        if float(qiwi['data'][0]['adv']['price']) < float(r['data'][0]['adv']['price']):
            r = qiwi
        rosbank = get_req("BUY", "RosBank")
        if float(rosbank['data'][0]['adv']['price']) < float(r['data'][0]['adv']['price']):
            r = rosbank

        userNo = r['data'][0]['advertiser']['userNo']
        tradeMethods = ''
        for methods in r['data'][0]['adv']['tradeMethods']:
            method = methods['identifier']
            tradeMethods += f'{method}\n'

        return ({
            "platform": "Binance",
            "maxLimit": r['data'][0]['adv']['maxSingleTransAmount'],
            "minLimit": r['data'][0]['adv']['minSingleTransQuantity'],
            "quantity": r['data'][0]['adv']['tradableQuantity'],
            "userName": r['data'][0]['advertiser']['nickName'],
            "price": float(r['data'][0]['adv']['price']),
            "tradeMethods": tradeMethods,
            "link": f'https://p2p.binance.com/ru/advertiserDetail?advertiserNo={userNo}'
        })

    def sell():
        r = get_req("SELL", "Tinkoff")
        qiwi = get_req("SELL", "QIWI")
        if float(qiwi['data'][0]['adv']['price']) > float(r['data'][0]['adv']['price']):
            r = qiwi
        rosbank = get_req("SELL", "RosBank")
        if float(rosbank['data'][0]['adv']['price']) > float(r['data'][0]['adv']['price']):
            r = rosbank

        userNo = r['data'][0]['advertiser']['userNo']
        tradeMethods = ''
        for methods in r['data'][0]['adv']['tradeMethods']:
            method = methods['identifier']
            tradeMethods += f'{method}\n'

        return ({
            "platform": "Binance",
            "maxLimit": r['data'][0]['adv']['maxSingleTransAmount'],
            "minLimit": r['data'][0]['adv']['minSingleTransQuantity'],
            "quantity": r['data'][0]['adv']['tradableQuantity'],
            "userName": r['data'][0]['advertiser']['nickName'],
            "price": float(r['data'][0]['adv']['price']),
            "tradeMethods": tradeMethods,
            "link": f'https://p2p.binance.com/ru/advertiserDetail?advertiserNo={userNo}'
        })
