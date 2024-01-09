import asyncio
from aiogram import types, F
from loader import dp, bot
from keyboards import inline
from utils import string


# Другое
@dp.callback_query(F.data == "other")
async def other(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                text=await string.menu(),
                                message_id=call.message.message_id,
                                disable_web_page_preview=True, reply_markup=await inline.other())


# Как пользоваться ботом?
@dp.callback_query(F.data == "manual")
async def manual(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                text=await string.manual(), parse_mode="MarkdownV2",
                                message_id=call.message.message_id,
                                disable_web_page_preview=True, reply_markup=await inline.backManual())

