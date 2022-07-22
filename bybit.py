from pprint import pprint
import requests

url = "https://api2.bybit.com/spot/api/otc/item/list"

headers = {
  'authority': 'api2.bybit.com',
  'accept': 'application/json',
  'accept-language': 'ru-RU',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'bm_sz=51171395F7009DF3BDF950106C48BDDC~YAAQrP1zPv6VbLWBAQAAlQmqIBB+s5DtBhAKT2z671/4M9gk2G3M5zV4FcMuILQq0iMkO7NTxoGrvFXxrZZhWou7Sw0X+6iiBzu7Xh23m/DBK8ywfFN1Szqw57/oXUpVOxGSquf2NZ/XgLlqShU3xNlO34bK88CZtyw7CjBV83NUWBW17e4P9T6xFScb93OJiwV2JzsACd4D2lXCucHpOCBGKVxY6px14nTuHpAslYldSfOxoF7PGNHiEm/MXcKUKv/vvs5aA1n+9Vp1T65acIyu8jd/rf1puyIxYWAI4TkBYg==~3422261~4405058; _gcl_au=1.1.1764091458.1658405391; _ga=GA1.2.1050810185.1658405391; _gid=GA1.2.2136854777.1658405391; _gat_UA-126371352-1=1; tmr_lvid=718b11584a3cc4af750ce00cb8fa0743; tmr_lvidTS=1658405391033; _by_l_g_d=6ad999c3-a892-cda6-100d-efeebb2e24e7; BYBIT_REG_REF_prod={"lang":"ru-RU","g":"6ad999c3-a892-cda6-100d-efeebb2e24e7","referrer":"away.vk.com/","source":"vk.com","medium":"other","url":"https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod="}; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218220aa0af5445-0375a3fe9867f2-1c525635-1764000-18220aa0af619c3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Faway.vk.com%2F%22%2C%22_a_u_v%22%3A%220.0.5%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgyMjBhYTBhZjU0NDUtMDM3NWEzZmU5ODY3ZjItMWM1MjU2MzUtMTc2NDAwMC0xODIyMGFhMGFmNjE5YzMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218220aa0af5445-0375a3fe9867f2-1c525635-1764000-18220aa0af619c3%22%7D; _ym_uid=16584053911016622631; _ym_d=1658405391; _ym_isad=1; bm_mi=CD9CB0B1C5681B8FFE32D5A5D0F2C847~YAAQrP1zPmqWbLWBAQAAmxCqIBDMtRf1t1CIOB9T1FaHACihltvbXoZQCELhi5oqY3v1oChnFW3ddqHMb9GHSXtE8zwSpVSiplbrpvNMH+ZyR5+G9z/d44FM2sPrTRL7DBFbB/nYUIhPe09zrJwIwz3zVhh4EeiEyZgwj7YKiBuVMX032KTFeQCo9B6yHIx7rUBMIj/isWOXxjZl5h5CVXRO59SjXrKiY/VyLHuOlNAuPdvhmLHOMVUldJcMJU+SOnQSzz5OAmuJIDiVBoyd66VK0q5tLFrY0DhmrfNhGeHS7AEobitXO+bILGrsyF4XpQimnsQzEF43h4QHcPdC9Hhq1PS7PrMW16wIFsJxO7o6Ntg=~1; _abck=0C487C9B41B425D4BADF20A1FFA1FA70~0~YAAQrP1zPoeWbLWBAQAAoBGqIAhZ8ymODCQKk26BZ3MIcrKyi5ghmlN8e2LGeNXDVxbizaOIPwxjqrNT7RRAZ8GBCZh5gDQ7QaQoTuRekzZQFf4ZvK4k4peE+4It133mQ/5od3InH2htJ4o3LOC3gf03ocgDv6O4vwketArJGcQAIgESxKy7QW1Mrdygp4fNpjQ9JTEisKuOTq6R1qQxodHM4sAGr6D+gvNtavIQwbvGVbKmZkb27dxK2oXa8VqJAGiQqq/tJXwyjofq6zX60lFwHUVlq2tdV0OGM/8pH48dKhUZ9buuqK+BXTDHQO51527Ax3V6MVyp4FAnYNh0FhuK+9mVGtaE0vkJwgURqUZ9iSfpqQYfd1bH5CNJ4p1zFxtTrCXrRrBRJu0WR+hOebmn2Klk8ng=~-1~-1~-1; b_t_c_k=; RT="z=1&dm=bybit.com&si=l7g6keki3l9&ss=l5uzr0wj&sl=1&tt=2ri&rl=1&ld=2rj"; ak_bmsc=940413AE0A6B8569A3C8BAE97435BE9A~000000000000000000000000000000~YAAQrP1zPkuXbLWBAQAAohqqIBBL7wKExdZLNiJVV4vj+G6jYQ6PQddCSgFVInoX6B3kG6RHw5ot8lciGaTtDq7XBMx0NM4xlw0zT1dT3/9QLUsuhmn7xl0VnbHHXHTVDXuMgbqdJKpSe0mAQeCWS/7clClWfkvVnSQS22xxQWUqHXoHlJG/LiBuPHiYsKtIuBQyYUOtd/cXel3VuldNkwB9Ax1206SJSayIr1/AwzEq382ROe31lc+AwUncmIl3SlIQqf3FvnBQ9s7LwsTe/Mru4t4GhCzWF1c0VSINvVf8FLZpSyx+g5To4oWpLNpJ5np1mGNGBTa3lYdAtMQ6PlP0r7r0OG3sOascvE+WWFd88wTUpuRmAcQJvktjOtSqPN2rT0xTb2rWlehlDZHBzf+r4ghMdZymIPEisvo7C1jv5C6DTYoZCcs3ORZoYe4aDhZNzDhWfWlf9lVCcDOADCXOJKrWI+3u+vzQrakQbdKj64Tg8AY+j06gicLqAyiXWI50xk5bIRc1Z2NOdm1ZAM+dgSHW4YI0q4RHhWHXFp79QsGJ6w==; bm_sv=B2335EB12E0C0E30B525719899059172~YAAQrP1zPjmYbLWBAQAA+CqqIBA80qyn7jCS5CpKb4Ri60XiocwgLQo4eg/xCx3/R9OtcqCymc1aiolqGDvyBSJ5L1n7SLRxa58OlWhJBdfj8Tpq1BW5Gmy7M8fbWrx2Q/jocizUqPVzVDk4aB2U7TomBq6Pvkct3huml/Zzy91MJfCr2fPCNmFbwb4yNSey5w+H6y+ToKVowDVvQigVqES0d3qbfAPRTeMypHa+FgfXyC+X0wtF3yDbOSIEbsk=~1; tmr_reqNum=4; _abck=0C487C9B41B425D4BADF20A1FFA1FA70~-1~YAAQRf1zPhaglLKBAQAAmcuqIAj9HSmVxU/O3b+iNcGz6qhW9zEorWwJX29rdxHQN+/gr7SqdACd5wVLxnzmi0zzGXmsbgKLuUExEqAmLkv/xYSgQX57htYldwm338eg0FwdmNVE5l36j2gz9JPyE//qSrB3rfJ7/s9i0yTlMzpUbgSzPZhCdhvRBUD4iwcQBZ3bYckg89IGaguFK44LsNhNxEk63oTTLNiehykNY7QY2cSEdYttkPYq2nuM9gvGve9CEgP3Vt9EhexZl2SaRrwB/68zSa6EFcBIr56A0gL9IsegIgxsBEg/spjiBp9jBWIDshD2/AAm8ytXfzKQdQNBdhZCJCdWHmtXv9pBRCp/3329zu5DSqv3Wywa7/8PiykfNs4P7F5u3E8BB5MnyrNojDgGvsM=~0~-1~-1',
  'guid': '6ad999c3-a892-cda6-100d-efeebb2e24e7',
  'lang': 'ru-RU',
  'origin': 'https://www.bybit.com',
  'platform': 'PC',
  'referer': 'https://www.bybit.com/',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

methods = {"75": "Tinkoff", "27": "FPS", "5": "Advcash", "90": "Cash in person", "14": "Bank Transfer", "185": "Rosbank", "162": "Skrill", "51": "Payeer", "111": "Neteller", "102": "Home Credit Bank", "64": "Raiffeisenbank", "62": "QIWI", "274": "Юmoney", "88": "Yandex Money"}

def getReq(type, method):
  payload=f'userId=&tokenId=USDT&currencyId=RUB&payment={method}&side={type}&size=10&page=1&amount='
  r = requests.request("POST", url, headers=headers, data=payload).json()['result']['items'][0]
  return r
  
class getBybit:
    def buy():
      r = getReq(1, 75)
      qiwi = getReq(1, 62) 
      if float(qiwi['price']) < float(r['price']):
          r = qiwi
      rosbank = getReq(1, 185)  
      if float(rosbank['price']) < float(r['price']):
        r = rosbank
          
      merchant = str(r['userId'])
      payMethods = r['payments']
      allPayMethods = ''
      for i in range(len(payMethods)):
        x = methods[f'{payMethods[i]}']
        allPayMethods+=f'{x}\n'
      return ({
              "platform": "Bybit",
              "maxLimit": r['maxAmount'],
              "minLimit": r['minAmount'],
              "quantity": r['lastQuantity'],
              "userName": r['nickName'],
              "price": float(r['price']),
              "tradeMethods": allPayMethods,
              "link": f'https://www.bybit.com/fiat/trade/otc/profile/{merchant}/USDT/RUB'
              })
        
    def sell():
        r = getReq(0, 75)
        qiwi = getReq(0, 62) 
        if float(qiwi['price']) > float(r['price']):
            r = qiwi
        rosbank = getReq(0, 185)  
        if float(rosbank['price']) > float(r['price']):
          r = rosbank
        
        merchant = str(r['userId'])
        payMethods = r['payments']
        allPayMethods = ''
        for i in range(len(payMethods)):
          x = methods[f'{payMethods[i]}']
          allPayMethods+=f'{x}\n'
        return ({
                "platform": "Bybit",
                "maxLimit": r['maxAmount'],
                "minLimit": r['minAmount'],
                "quantity": r['lastQuantity'],
                "userName": r['nickName'],
                "price": float(r['price']),
                "tradeMethods": allPayMethods,
                "link": f'https://www.bybit.com/fiat/trade/otc/profile/{merchant}/USDT/RUB'
                })
      