from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo



search_user = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='🕵️ Поиск пользователя', web_app=WebAppInfo(url=f'https://ya.ru/'))
                                    ]
                                ])















#
# # async def menu():
# #     kb = InlineKeyboardMarkup(
# #         keyboard=[
# #             InlineKeyboardButton(text='Найти пользователя 🔎', callback_data='searchUser'),
# #             InlineKeyboardButton(text='Мой профиль 📎', callback_data='profile'),
# #             InlineKeyboardButton(text='Активные сделки 📂', callback_data='activeTrades'),
# #             InlineKeyboardButton(text='Другое ⚙️', callback_data='other')
# #         ]
# #     )
# #     return menu(*kb)
#
#
# async def menu():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     searchUser = InlineKeyboardButton(text='Найти пользователя 🔎', callback_data='searchUser')
#     profile = InlineKeyboardButton(text='Мой профиль 📎', callback_data='profile')
#     activeTrades = InlineKeyboardButton(text='Активные сделки 📂', callback_data='activeTrades')
#     other = InlineKeyboardButton(text='Другое ⚙️', callback_data='other')
#     keyboard.add(searchUser, profile, activeTrades, other)
#
#     return keyboard
#
#
# async def back():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     back = InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     keyboard.add(back)
#     return keyboard
#
#
# async def backActiveTrades():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     back = InlineKeyboardButton(text='Назад ↩', callback_data='backActiveTrades')
#     keyboard.add(back)
#     return keyboard
#
#
# async def profile():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
#     deposit = InlineKeyboardButton(text='Пополнить ➕', callback_data='deposit')
#     withdraw = InlineKeyboardButton(text='Вывести ➖', callback_data='withdraw')
#     back = InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     keyboard.add(deposit, withdraw, back)
#     return keyboard
#
#
# async def search():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     deal = InlineKeyboardButton(text='Начать сделку 💲', callback_data='deal')
#     back = InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     keyboard.add(deal, back)
#     return keyboard
#
#
# async def crypto():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='🟪 Toncoin (TON)', callback_data='TON'),
#         InlineKeyboardButton(text='🟩 Tether (USDT)', callback_data='USDT'),
#         InlineKeyboardButton(text='🟨 Binance USD (BUSD)', callback_data='BUSD'),
#         InlineKeyboardButton(text='🟦 USD Coin (USDC)', callback_data='USDC'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     )
#     return keyboard
#
#
# async def dealCrypto():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='🟪 Toncoin (TON)', callback_data='TONdeal'),
#         InlineKeyboardButton(text='🟩 Tether (USDT)', callback_data='USDTdeal'),
#         InlineKeyboardButton(text='🟨 Binance USD (BUSD)', callback_data='BUSDdeal'),
#         InlineKeyboardButton(text='🟦 USD Coin (USDC)', callback_data='USDCdeal'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     )
#     return keyboard
#
#
# async def assured():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='Да ✅', callback_data='assured'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     )
#     return keyboard
#
#
# async def check():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='Я оплатил ✅', callback_data='paid'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     )
#     return keyboard
#
#
# async def sendDeal():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='Отправить ✅', callback_data='sendDeal'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     )
#     return keyboard
#
#
# async def withdraw():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='Админ 👀🦈', url="https://t.me/rixittt"),
#         InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     )
#     return keyboard
#
#
# async def activeTrades():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
#     keyboard.add(
#         InlineKeyboardButton(text='Покупка 🛒', callback_data='buy'),
#         InlineKeyboardButton(text='Продажа 📦', callback_data='sell'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='back')
#     )
#     return keyboard
#
#
# async def buyDeal():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='Оплатить 💸', callback_data='payment'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='backActiveTrades')
#     )
#     return keyboard
#
#
# async def buyDealnext():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
#     keyboard.add(
#         InlineKeyboardButton(text='Оплатить 💸', callback_data='payment'),
#         InlineKeyboardButton(text='Далее ↪️', callback_data='nextBuy'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='backActiveTrades'))
#     return keyboard
#
#
# async def sellDeal():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='Отменить сделку ❌', callback_data='cancelDeal'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='backActiveTrades')
#     )
#     return keyboard
#
#
# async def sellDealnext():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
#     keyboard.add(
#         InlineKeyboardButton(text='Отменить сделку ❌', callback_data='cancelDeal'),
#         InlineKeyboardButton(text='Далее ↪️', callback_data='nextSell'),
#         InlineKeyboardButton(text='Назад ↩', callback_data='backActiveTrades'))
#     return keyboard
#
#
# async def other():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='Как пользоваться ботом? 🤖', callback_data='manual'),
#         InlineKeyboardButton(text='Поддержка ☎️', url="https://t.me/rixittt"),
#         InlineKeyboardButton(text='Назад ↩', callback_data='back'))
#     return keyboard
#
#
# async def backManual():
#     keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     keyboard.add(
#         InlineKeyboardButton(text='Поддержка ☎️', url="https://t.me/rixittt"),
#         InlineKeyboardButton(text='Назад ↩', callback_data='back'))
#     return keyboard
#
