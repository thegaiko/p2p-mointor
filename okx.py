from pprint import pprint
import requests

url = "https://www.okx.com/v3/c2c/tradingOrders/books?t=1658405145766&quoteCurrency=RUB&baseCurrency=USDT&side=buy&paymentMethod=all&userType=all&showTrade=false&showFollow=false&showAlreadyTraded=false&isAbleFilter=false&urlId=4"

headers = {
  'authority': 'www.okx.com',
  'accept': 'application/json',
  'accept-language': 'ru-RU',
  'app-type': 'web',
  'cookie': 'locale=ru_RU; __cf_bm=xZ_c2OTs0yObswvowBBc5bJblujgJvUi_3gW1J04E_Y-1658405008-0-AT+C+c5/o0Clfs0RfBUe2cecw549Pl8OMMAUAJiexoWOAcIlalYcYoUVedD4E901jpNxVAqv8+n+TcSv8MKxc/4=; first_ref=https%3A%2F%2Faway.vk.com%2F; _gcl_au=1.1.208113577.1658405009; _ga=GA1.2.2064396576.1658405009; _gid=GA1.2.900310712.1658405009; amp_56bf9d=zCw_PNv-FDMrW8tSfIFYY0...1g8ga8din.1g8ga90mp.0.1.1; amp_56bf9d_okx.com=zCw_PNv-FDMrW8tSfIFYY0...1g8ga8din.1g8ga90ms.4.1.5',
  'devid': 'e66a2415-65b0-4c8a-a4f3-c98ecb5ed763',
  'referer': 'https://www.okx.com/ru/p2p-markets/rub/buy-usdt',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
  'x-cdn': 'https://static.okx.com',
  'x-utc': '3'
}

def getReq(type, method):
    url = f'https://www.okx.com/v3/c2c/tradingOrders/books?t=1658405145766&quoteCurrency=RUB&baseCurrency=USDT&side={type}&paymentMethod={method}&userType=all&showTrade=false&showFollow=false&showAlreadyTraded=false&isAbleFilter=false&urlId=4'
    r = requests.request("GET", url, headers=headers)
    r = r.json()['data'][type][0]
    return r

class getOkx:
    def buy():
        r = getReq('sell', 'Tinkoff')
        qiwi = getReq('sell', 'QiWi') 
        if float(qiwi['price']) < float(r['price']):
            r = qiwi
        rosbank = getReq('sell', 'Rosbank')  
        if float(rosbank['price']) < float(r['price']):
          r = rosbank
        
        merchantId = r['merchantId']
        if merchantId == '':
            link = 'https://www.okx.com/ru/p2p-markets/rub/buy-usdt'
        else:
            link = f'https://www.okx.com/ru/p2p/ads-merchant?merchantId={merchantId}'
        
            
        methods = r['paymentMethods']
        tradeMethods = ''
        for method in methods:
            tradeMethods += f'{method}\n'
        return ({
            "platform": "Okx",
            "maxLimit": r['quoteMinAmountPerOrder'],
            "minLimit": r['quoteMaxAmountPerOrder'],
            "quantity": r['availableAmount'],
            "userName": r['nickName'],
            "price": float(r['price']),
            "tradeMethods": tradeMethods,
            "link": link
            })

    def sell():
        r = getReq('buy', 'Tinkoff')
        qiwi = getReq('buy', 'QiWi') 
        if float(qiwi['price']) > float(r['price']):
            r = qiwi
        rosbank = getReq('buy', 'Rosbank')  
        if float(rosbank['price']) > float(r['price']):
          r = rosbank

        
        merchantId = r['merchantId']
        if merchantId == '':
            link = 'https://www.okx.com/ru/p2p-markets/rub/sell-usdt'
        else:
            link = f'https://www.okx.com/ru/p2p/ads-merchant?merchantId={merchantId}'
            
        methods = r['paymentMethods']
        tradeMethods = ''
        for method in methods:
            tradeMethods += f'{method}\n'
        return ({
            "platform": "Okx",
            "maxLimit": r['quoteMinAmountPerOrder'],
            "minLimit": r['quoteMaxAmountPerOrder'],
            "quantity": r['availableAmount'],
            "userName": r['nickName'],
            "price": float(r['price']),
            "tradeMethods": tradeMethods,
            "link": link
            })
    
