import requests

url = "https://discord.com/api/webhooks/1011647486877782096/fkKWnmISgMqkcf25tT_Nb2cF8kXbpVpZjMWNWz2xzxSiu78w1xPnh59QDRoGPHBxdtU-"

def startHook():
    data = {"username": "Arbitration", "embeds": [
        {
            "description": "**P2P MONITOR STARTED**",
            "color": 16755968,
            "footer": {
                "text": "Essential Investments x Gaiko",
                "icon_url": "https://sun9-24.userapi.com/impg/opayMYZj60Se_3vV2ki13qkh_bCiULoZkIrZRQ/leNz2i2sb7o.jpg?size=2500x2500&quality=95&sign=2c2fef7af8e3adfa9eb22716dd7926e8&type=album"
            }
        }
    ]}

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))



def sendHook(buy, sell):
    buyPlatform = buy['platform']
    sellPlatform = sell['platform']

    buyNickname = buy['userName']
    sellNickname = sell['userName']

    buyPrice = buy['price']
    sellPrice = sell['price']
    total = sellPrice - buyPrice

    buyQuantity = buy['quantity']
    sellMinLimit = sell['minLimit']
    sellMaxLimit = sell['maxLimit']

    methodsBuy = buy['tradeMethods']
    methodsSell = sell['tradeMethods']

    buyLink = buy['link']
    sellLink = sell['link']

    data = {"username": "Arbitration", "embeds": [
        {
            "title": f'{buyPlatform} - {sellPlatform}',
            "description": f'{buyNickname} - {sellNickname}',
            "color": 16755968,
            "fields": [
                {
                    "name": "Spread",
                    "value": f'**{buyPlatform}**: {buyPrice}\n**{sellPlatform}**: {sellPrice}\n**Total**: {total}',
                    "inline": True
                },
                {
                    "name": "Available USDT",
                    "value": buyQuantity,
                    "inline": True
                },
                {
                    "name": "Limits",
                    "value": f'₽{sellMinLimit} - ₽{sellMaxLimit}'
                },
                {
                    "name": "Payment Method for buy",
                    "value": methodsBuy,
                    "inline": True
                },
                {
                    "name": "Payment Method for sell",
                    "value": methodsSell,
                    "inline": True
                },
                {
                    "name": "Links",
                    "value": f'Buy order link - [{buyPlatform}]({buyLink})\n Sell order link - [{sellPlatform}]({sellLink})',
                }],
            "footer": {
                "text": "Essential Investments x Gaiko",
                "icon_url": "https://sun9-24.userapi.com/impg/opayMYZj60Se_3vV2ki13qkh_bCiULoZkIrZRQ/leNz2i2sb7o.jpg?size=2500x2500&quality=95&sign=2c2fef7af8e3adfa9eb22716dd7926e8&type=album"
            },
        }
    ]}

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))