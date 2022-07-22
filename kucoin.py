from pprint import pprint
import requests

payload={}
headers = {
  'authority': 'www.kucoin.com',
  'accept': 'application/json',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': '__cfruid=7417d287f6f8e03c80723f6474149dd0476ea960-1658405260; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218220a80d821b78-05377bf62ad79dc-1c525635-1764000-18220a80d831b95%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Faway.vk.com%2F%22%7D%2C%22%24device_id%22%3A%2218220a80d821b78-05377bf62ad79dc-1c525635-1764000-18220a80d831b95%22%7D; _ga=GA1.2.1238600791.1658405261; _gid=GA1.2.1458057730.1658405261; _gat=1; x-bullet-token=2neAiuYvAU5cbMXpmsXD5OJlewXCKryg8dSpDCgag8ZwbZpn3uIHi0A1AOtpCibAwoXOiOG0Q0EImLT1qzoVMQeeD0HEiM0c10fG04HHMSLzSxbXZS9VLKqRyqznCVt1whuoNZhpWWFwFoy5ltFz_DERK6FXhwcv.4AWrhFNY_vbniLcCZxpA2g==; __cf_bm=wecTGjvzPwwcWjGrAaHhK6OqBc3NkbD3PdT9aGGqe7E-1658405274-0-AcHlXRyngWgLMJvlhcvmhd4pXXTzbnX9/AVzarQRclpNWQxkaZr68kd5GjRQj5IgFLpP/Vbx4N1x+a+bqyxg18MdapRb61eLp9ZcesIcTuyd1ECW1flZ+mB7CqCddEGc3w==; AWSALB=u03eSOEsmg2HG63vT0CA4vIK5pY+SogVsWPLONgmUj//uSMCmAOQ49cBRfkL3oSULcRUj950yZqsogoM9QBK9l1eGSceYRWFMz6tGmCxbWQfYeEoGnxdo04MlYSC; AWSALBCORS=u03eSOEsmg2HG63vT0CA4vIK5pY+SogVsWPLONgmUj//uSMCmAOQ49cBRfkL3oSULcRUj950yZqsogoM9QBK9l1eGSceYRWFMz6tGmCxbWQfYeEoGnxdo04MlYSC; AWSALB=rgW9xx7XerravId/qpoahCg0vcJA9A86p/B6o4Z7jQTbtioxsQSwyZTdD/aoLH4Wb6yC4pF6YP09t02pGaXQgf/rRaKBQvDFNLg/l1vwpU6oVHCuvC/i3BDGC+6w; AWSALBCORS=rgW9xx7XerravId/qpoahCg0vcJA9A86p/B6o4Z7jQTbtioxsQSwyZTdD/aoLH4Wb6yC4pF6YP09t02pGaXQgf/rRaKBQvDFNLg/l1vwpU6oVHCuvC/i3BDGC+6w',
  'referer': 'https://www.kucoin.com/ru/otc/buy/USDT-RUB',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

class getKucoin:
    def buy():
        url = "https://www.kucoin.com/_api/otc/ad/list?currency=USDT&side=BUY&legal=RUB&page=1&pageSize=10&status=PUTUP&lang=ru_RU"
        r = requests.request("GET", url, headers=headers, data=payload)
        r = r.json()['items'][0]
        tradeMethods = ''
        adPayTypes = r['adPayTypes']
        for bankName in adPayTypes:
          type = (bankName['reservedFields'])
          count = len(type)
          if count > 2:
            for i in range(16, count-2):
              tradeMethods+=type[i]
            tradeMethods+=('\n')
        return ({
                "platform": "Kucoin",
                "maxLimit": r['limitMaxQuote'],
                "minLimit": r['limitMinQuote'],
                "quantity": r['currencyBalanceQuantity'],
                "userName": r['nickName'],
                "price": float(r['premium']),
                "tradeMethods": tradeMethods,
                "link": f'https://www.kucoin.com/ru/otc/buy/USDT-RUB'
                })
    def sell():
        url = "https://www.kucoin.com/_api/otc/ad/list?currency=USDT&side=SELL&legal=RUB&page=1&pageSize=10&status=PUTUP&lang=ru_RU"
        r = requests.request("GET", url, headers=headers, data=payload)
        r = r.json()['items'][0]
        tradeMethods = ''
        adPayTypes = r['adPayTypes']
        for bankName in adPayTypes:
          type = (bankName['reservedFields'])
          count = len(type)
          if count > 2:
            for i in range(16, count-2):
              tradeMethods+=type[i]
            tradeMethods+=('\n')
        return ({
                "platform": "Kucoin",
                "maxLimit": r['limitMaxQuote'],
                "minLimit": r['limitMinQuote'],
                "quantity": r['currencyBalanceQuantity'],
                "userName": r['nickName'],
                "price": float(r['premium']),
                "tradeMethods": tradeMethods,
                "link": f'https://www.kucoin.com/ru/otc/sell/USDT-RUB'
                })