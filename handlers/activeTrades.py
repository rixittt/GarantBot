from aiogram import types, F
from loader import dp, bot
from database import DB
from keyboards import inline
from utils import string, parserTON


# Активные сделки
@dp.callback_query(F.data == ["activeTrades", "backActiveTrades"])
async def activeTrades(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                text="<b> 📂 Выберите тип сделки: </b>",
                                message_id=call.message.message_id,
                                disable_web_page_preview=True, reply_markup=await inline.activeTrades())


# Мои сделки на покупку
@dp.callback_query(F.data == "buy")
async def buy(call: types.CallbackQuery):
    if await DB.selectDealBuy(call.from_user.id):
        if len(await DB.selectDealBuy(call.from_user.id)) <= 1:
            button = await inline.buyDeal()
        else:
            button = await inline.buyDealnext()

        dealInfo = str(await DB.selectDealBuy(call.from_user.id)).replace("[", "").replace("]", "").replace("(",
                                                                                                            "").replace(
            ")", "").replace(",", "").replace("'", "").split()

        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    text=await string.deal(dealInfo[0], call.from_user.id,
                                                           await DB.selectName(call.from_user.id), dealInfo[1],
                                                           await DB.selectName(dealInfo[1]), dealInfo[2], dealInfo[3]),
                                    message_id=call.message.message_id, parse_mode="MarkdownV2",
                                    disable_web_page_preview=True, reply_markup=button)

    else:
        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    text="*Покупка 🛒*\n\n_У вас нет активных сделок\!_",
                                    message_id=call.message.message_id, parse_mode="MarkdownV2",
                                    disable_web_page_preview=True, reply_markup=await inline.backActiveTrades())


# Моя следующая сделка на покупку
@dp.callback_query(F.data == "nextBuy")
async def nextBuy(call: types.CallbackQuery):
    if len(list(await DB.selectDealBuy(call.from_user.id))) <= await DB.selectNext(call.from_user.id):
        await DB.updateNext(call.from_user.id, 1)
        button = await inline.buyDeal()
    else:
        button = await inline.buyDealnext()

    dealInfo = list(await DB.selectDealBuy(call.from_user.id))[await DB.selectNext(call.from_user.id)]

    await DB.updateNext(call.from_user.id, await DB.selectNext(call.from_user.id) + 1)

    await bot.edit_message_text(chat_id=call.message.chat.id,
                                text=await string.deal(dealInfo[0][0], call.from_user.id,
                                                       await DB.selectName(call.from_user.id), dealInfo[0][1],
                                                       await DB.selectName(dealInfo[0][1]), dealInfo[0][2],
                                                       dealInfo[0][3]),
                                message_id=call.message.message_id, parse_mode="MarkdownV2",
                                disable_web_page_preview=True, reply_markup=button)


# Мои сделки на продажу
@dp.callback_query(F.data == "sell")
async def sell(call: types.CallbackQuery):
    if await DB.selectDealSell(call.from_user.id):
        if len(await DB.selectDealSell(call.from_user.id)) <= 1:
            button = await inline.sellDeal()
        else:
            button = await inline.sellDealnext()

        dealInfo = str(await DB.selectDealSell(call.from_user.id)).replace("[", "").replace("]", "").replace("(",
                                                                                                             "").replace(
            ")", "").replace(",", "").replace("'", "").split()

        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    text=await string.deal(dealInfo[0], dealInfo[1],
                                                           await DB.selectName(dealInfo[1]), call.from_user.id,
                                                           await DB.selectName(call.from_user.id), dealInfo[2],
                                                           dealInfo[3]),
                                    message_id=call.message.message_id, parse_mode="MarkdownV2",
                                    disable_web_page_preview=True, reply_markup=button)

    else:
        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    text="*Продажа 📦*\n\n_У вас нет активных сделок\!_",
                                    message_id=call.message.message_id, parse_mode="MarkdownV2",
                                    disable_web_page_preview=True, reply_markup=await inline.backActiveTrades())


# Моя следующая сделка на родажу
@dp.callback_query(F.data == "nextSell")
async def nextSell(call: types.CallbackQuery):
    if len(list(await DB.selectDealSell(call.from_user.id))) <= await DB.selectNext(call.from_user.id):
        await DB.updateNext(call.from_user.id, 1)
        button = await inline.sellDeal()
    else:
        button = await inline.sellDealnext()

    dealInfo = list(await DB.selectDealSell(call.from_user.id))[await DB.selectNext(call.from_user.id)]

    await DB.updateNext(call.from_user.id, await DB.selectNext(call.from_user.id) + 1)

    await bot.edit_message_text(chat_id=call.message.chat.id,
                                text=await string.deal(dealInfo[0][0], call.from_user.id,
                                                       await DB.selectName(call.from_user.id), dealInfo[0][1],
                                                       await DB.selectName(dealInfo[0][1]), dealInfo[0][2],
                                                       dealInfo[0][3]),
                                message_id=call.message.message_id, parse_mode="MarkdownV2",
                                disable_web_page_preview=True, reply_markup=button)


# Оплатить сделку
@dp.callback_query(F.data == "payment")
async def payment(call: types.CallbackQuery):
    deal_id = call.message.text.split()[3]

    dealInfo = str(await DB.selectFromAllDeal(deal_id)).replace("[", "").replace("]", "").replace(",", "").replace("'",
                                                                                                                   "").replace(
        "(", "").replace(")", "").split()

    if dealInfo:
        await DB.updateBalance(dealInfo[0], dealInfo[2],
                               int(await DB.selectSum(dealInfo[0], dealInfo[2])) + int(dealInfo[1]))

        await DB.delateAllDeal(deal_id)

        await DB.updateQuantityBuy(call.from_user.id, await DB.selectQuantityBuy(call.from_user.id) + 1)

        await DB.updateQuantitySell(dealInfo[0], await DB.selectQuantitySell(dealInfo[0]) + 1)

        if dealInfo[2] == "TON":
            sum = await parserTON.Currency.get_currency_price() * int(dealInfo[1]) + await DB.selectBuyUSD(
                call.from_user.id)
        else:
            sum = int(dealInfo[1]) + await DB.selectBuyUSD(call.from_user.id)

        await DB.updateBuyUSD(call.from_user.id, sum)

        await DB.updateSellUSD(dealInfo[0], sum)

        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    text="💸*_Сделка успешно оплачена\!_*\n_Спасибо\! ☺️_",
                                    message_id=call.message.message_id, parse_mode="MarkdownV2",
                                    disable_web_page_preview=True, reply_markup=await inline.back())

        await bot.send_message(dealInfo[0],
                               await string.dealConfirm(await DB.selectName(call.from_user.id), dealInfo[1],
                                                        dealInfo[2], await DB.selectTON(dealInfo[0]),
                                                        await DB.selectUSDT(dealInfo[0]),
                                                        await DB.selectBUSD(dealInfo[0]),
                                                        await DB.selectUSDC(dealInfo[0])), parse_mode="MarkdownV2",
                               reply_markup=await inline.back())
    else:
        await bot.send_message(call.from_user.id, "_Сделка уже осуществлена\!_☺️", parse_mode="MarkdownV2",
                               reply_markup=await inline.back())


# Отменить сделку
@dp.callback_query(F.data== "cancelDeal")
async def cancelDeal(call: types.CallbackQuery):
    deal_id = call.message.text.split()[3]

    dealInfo = str(await DB.selectUserIdFromAllDeal(deal_id)).replace("[", "").replace("]", "").replace(",",
                                                                                                        "").replace("'",
                                                                                                                    "").replace(
        "(", "").replace(")", "").split()

    await DB.updateBalance(dealInfo[0], dealInfo[2], await DB.selectSum(dealInfo[0], dealInfo[2]) + int(dealInfo[1]))

    await DB.delateAllDeal(deal_id)

    await bot.edit_message_text(chat_id=call.message.chat.id,
                                text="❌*_Сделка успешно отменена\!_*",
                                message_id=call.message.message_id, parse_mode="MarkdownV2",
                                disable_web_page_preview=True, reply_markup=await inline.back())

    await bot.send_message(dealInfo[0],
                           f"*_Сделака от пользователя {await DB.selectName(call.from_user.id)} отменена\!_*\n*На ваш баланс вернулась сумма в размере _{dealInfo[1]} {dealInfo[2]}_*",
                           parse_mode="MarkdownV2", reply_markup=await inline.back())
