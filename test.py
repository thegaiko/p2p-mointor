import requests

url = "https://discord.com/api/webhooks/999819135364104263/6urNwxE_rI24Ke-NdgWPUDGumSG4Lwjvqcuj65p6qtuxzGUWADfYfk2G1wsWx68hynKa"


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
    
    data = {
        "username" : "custom username"
    }
    data["embeds"] = [
        {
            "title": f'{buyPlatform} - {sellPlatform}',
            "description": f'{buyNickname} - {sellNickname}',
            "color": 12910592,
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
                "value": f'[{buyPlatform}]({buyLink})\n[{sellPlatform}]({sellLink})',
                }],
                "footer": {
                    "text": "ARBIT",
                    "icon_url": "https://sun9-58.userapi.com/impf/jgOkfU_yUf-HUS1_zd73z61ZpJZi1l6l6PxRjA/JtNJ-75JJtY.jpg?size=1624x1624&quality=95&sign=c4820a07df07b1312763693a050d833d&type=album"
                },
                }
    ]

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
    