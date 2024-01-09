from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart

from loader import dp, bot
from database import DB
from keyboards import inline, default
from utils import string


# Команда старт
@dp.message(F.text == '/start')
async def start(message: types.message):
    user = await DB.select_user_id(message.from_user.id)
    userDeal = await DB.select_user_idDeal(message.from_user.id)

    if message.from_user.username:
        name = "@" + message.from_user.username
    else:
        name = message.from_user.last_name + " " + message.from_user.first_name

    if not user or not userDeal:
        await DB.add_user_id(message.from_user.id)
        await DB.update_userName(message.from_user.id, name)

        await DB.add_user_idDeal(message.from_user.id)

    await bot.send_message(message.from_user.id, await string.menu(),
                           reply_markup=default.main_kb, parse_mode="html")



# Назад в меню
@dp.callback_query(F.data == "back")
async def back(call: types.CallbackQuery):
    try:
        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    text=await string.menu(),
                                    message_id=call.message.message_id, parse_mode="html",
                                    disable_web_page_preview=True, reply_markup=await inline.menu())
    except:
        await call.message.delete()
        await bot.send_message(call.from_user.id, await string.menu(),
                               reply_markup=await inline.menu(), parse_mode="html")
