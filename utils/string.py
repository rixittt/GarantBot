from database import DB


async def menu():
    return f"""<b>🦈🥷🏻 Привет!</b>

🤖 Я гарант-бот <b>@username</b>

<b>💳 Комиссия взымается только при выводе средств!</b>
 В размере <b>4%.</b>


<b>🧮 Количество активных пользователей в боте: {await DB.selectUserQuantity()}</b>
"""


async def profile(user_id, name, TON, USDT, BUSD, USDC, quantitySell, quantityBuy, sellUSD, buyUSD):
    return f"""*🔹Об аккаунте🔹* ⁠ ⁠ ⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠ ⁠ ⁠  ⁠ ⁠ ⁠⁠⁠ ⁠ ⁠ ⁠⁠ ⁠ ⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠ ⁠ ⁠  ⁠ ⁠ ⁠⁠⁠⁠ ⁠ ⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠ ⁠ ⁠  ⁠ ⁠ ⁠⁠
_ID аккаунта:_ `{user_id}`


*🔹Баланс🔹*
_Toncoin:_ {TON} TON
_Teather:_ {USDT} USDT
_Binance USD:_ {BUSD} BUSD
_USD Coin:_ {USDC} USDC


*🔹Сделок🔹*
_Продаж:_ {quantitySell} шт
_Покупок:_ {quantityBuy} шт

_Продаж в USD:_ {sellUSD} USD
_Покупок в USD:_ {buyUSD} USD
"""


async def searchUser(user_id, name, quantitySell, quantityBuy, sellUSD, buyUSD):
    return f"""*🔹Пользователь🔹* ⁠ ⁠ ⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠ ⁠ ⁠  ⁠ ⁠ ⁠⁠⁠ ⁠ ⁠ ⁠⁠ ⁠ ⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠ ⁠ ⁠  ⁠ ⁠ ⁠⁠⁠⁠ ⁠ ⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠⁠ ⁠ ⁠ ⁠ ⁠  ⁠ ⁠ ⁠⁠
_ID аккаунта:_ `{user_id}`


*🔹Сделок🔹*
_Продаж:_ {quantitySell} шт
_Покупок:_ {quantityBuy} шт

_Продаж в USD:_ {sellUSD} USD
_Покупок в USD:_ {buyUSD} USD
"""


async def deal(deal_id, user_id, name, user_idDeal, nameDeal, sum, currency):
    return f"""🛠 _ID сделки:_ `{deal_id}`
    
*🔹Покупатель🔹*
_ID аккаунта:_ `{user_id}`
_Сума сделки:_ *{sum} {currency}*

➖➖➖➖➖➖➖➖➖➖➖➖➖➖
*🔹Продавец🔹*
_ID аккаунта:_ `{user_idDeal}`
"""


async def dealConfirm(name, sum, currency, TON, USDT, BUSD, USDC):
    return f"""*Сделка ёот _{name}_ успешно оплачена\!*

*Сума сделки:* _{sum} {currency}_

*🔹Баланс🔹*
_Toncoin:_ {TON} TON
_Teather:_ {USDT} USDT
_Binance USD:_ {BUSD} BUSD
_USD Coin:_ {USDC} USDC


"""


async def manual():
    return f"""*_🤖 Как пользоваться ботом?_*
    
*💵 Для начала необходимо пополнить баланс\!*

*Далее нажимаете "Найти пользователя 🔎"*
*✉️ Вводите ID продавца, он должен вам его отправить*

*Затем снизу появится кнопка "Начать сделку 💲"
После получения и проверки того, что вы хотите купить,
нажимаете "Оплатить 💸"*
*Поздравляю\! Сделка успешно оплачена\!*


_❗️В случае если Вам дали невалидный товар и продавец
отказывается заменять или отклонять сделку
Вы можете решить вопрос через Тех\. Поддержку_

🔄 Если вы изменили свой @username, напишите пожалуйста нам\!
"""


async def botinfoMain():
    return f"""/botinfo - все комманды бота
    
/addadmin ай ди админа - добавление админа
/delateadmin ай ди админа - удаление админа

/send текст - рассылка

/add количество человек - добавление количество человек в бота

/TON количество TON - добавление баланса(TON)
/USDT количество USDT - добавление баланса(USDT)
/BUSD количество BUSD - добавление баланса(BUSD)
/USDC количество USDC - добавление баланса(USDC)

/delateTON - удаление баланса(TON)
/delateUSDT - удаление баланса(USDT)
/delateBUSD - удаление баланса(BUSD)
/delateUSDC - удаление баланса(USDC)

"""


async def botinfo():
    return f"""/botinfo - все комманды бота

/TON количество TON - добавление баланса(TON)
/USDT количество USDT - добавление баланса(USDT)
/BUSD количество BUSD - добавление баланса(BUSD)
/USDC количество USDC - добавление баланса(USDC)

/delateTON - удаление баланса(TON)
/delateUSDT - удаление баланса(USDT)
/delateBUSD - удаление баланса(BUSD)
/delateUSDC - удаление баланса(USDC)
"""
