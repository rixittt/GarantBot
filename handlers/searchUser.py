
from aiogram import types, F
from aiogram.fsm.context import FSMContext

from loader import dp, bot
from database import DB
from keyboards import default, inline
from state import states
from texts import search_text
from utils import string
from random import randint




@dp.message(F.text == "🔍 Поиск")
async def search(message: types.Message):
    photo1 = 'https://imgur.com/a/pcFkHTA'
    await bot.send_photo(message.from_user.id, photo1, caption=search_text, reply_markup=inline.search_user)



# Поиск пользователя
# @dp.message(F.text == "🔍 Поиск")
# async def search(call: types.CallbackQuery):
#     await bot.send_message(call.from_user.id,
#                            f"<b>✏️ Напишите ID пользователя:\n\nВаш ID: <code>{call.from_user.id}</code></b>", parse_mode="html")
#
#     await states.search.user_id.set()


# @F.message(state=states.search.user_id)
# async def state(message: types.Message, state: FSMContext):
#     if message.text == 'Назад ↩':
#         await state.finish()
#
#         wait = await bot.send_message(message.chat.id, '<b>Секунду...</b>', parse_mode="html",
#                                       reply_markup=default.remove)
#         await wait.delete()
#
#         await bot.send_message(message.chat.id, await string.menu(), parse_mode="html",
#                                reply_markup=await inline.menu())
#
#     elif message.text.isdigit() is False:
#         await bot.send_message(message.chat.id, "<b>Такого пользователя не существует! 🚫</b>", parse_mode="html")
#
#     else:
#
#         if int(message.text) != message.from_user.id:
#
#             check = False
#
#             for i in await DB.selectAllUser():
#                 if str(i) == message.text:
#                     check = True
#                     break
#
#             if check:
#                 await state.finish()
#                 user_id = message.text
#
#                 file = await bot.get_user_profile_photos(user_id=user_id)
#
#                 wait = await bot.send_message(message.chat.id, '<b>Секунду...</b>', parse_mode="html",
#                                               reply_markup=default.remove)
#                 await wait.delete()
#
#                 try:
#                     photo = await bot.get_file(file.photos[-1][-1].file_id)
#
#                     await bot.send_photo(message.chat.id, photo.file_id,
#                                          caption=await string.searchUser(user_id, await DB.selectName(user_id),
#                                                                          await DB.selectQuantitySell(user_id),
#                                                                          await DB.selectQuantityBuy(user_id),
#                                                                          await DB.selectSellUSD(user_id),
#                                                                          await DB.selectBuyUSD(user_id)),
#                                          reply_markup=await inline.search(), parse_mode="MarkdownV2")
#                 except:
#                     await bot.send_message(message.from_user.id,
#                                            await string.searchUser(user_id, await DB.selectName(user_id),
#                                                                    await DB.selectQuantitySell(user_id),
#                                                                    await DB.selectQuantityBuy(user_id),
#                                                                    await DB.selectSellUSD(user_id),
#                                                                    await DB.selectBuyUSD(user_id)),
#                                            parse_mode="MarkdownV2", reply_markup=await inline.search())
#
#                 await DB.update_user_idDeal(message.from_user.id, user_id)
#
#             else:
#                 await bot.send_message(message.chat.id, "<b>Такого пользователя не существует! 🚫</b>",
#                                        parse_mode="html")
#
#         else:
#             await bot.send_message(message.chat.id, "<b>Это ваш ID ☺️</b>", parse_mode="html")
#
#
# # Начать сделку
# @dp.callback_query(F.data =="deal")
# async def deal(call: types.CallbackQuery):
#     try:
#         await bot.edit_message_text(chat_id=call.message.chat.id,
#                                     text=f"<b>💵 Выберите валюту сделки:</b>",
#                                     message_id=call.message.message_id, parse_mode="html",
#                                     disable_web_page_preview=True, reply_markup=await inline.dealCrypto())
#     except:
#         await call.message.delete()
#         await bot.send_message(call.message.chat.id, f"<b>💵 Выберите валюту сделки:</b>", parse_mode="html",
#                                reply_markup=await inline.dealCrypto())
#
#
# @dp.callback_query(F.data ==["TONdeal", "USDTdeal", "BUSDdeal", "USDCdeal"])
# async def currencyDeal(call: types.CallbackQuery):
#     await call.message.delete()
#     await DB.update_currencyDeal(call.from_user.id, call.data.replace("deal", ""))
#
#     await bot.send_message(call.from_user.id, f"<b>💰 Введите сумму сделки в ({call.data.replace('deal', '')}) !</b>",
#                            parse_mode="html",
#                            reply_markup=await default.back())
#
#     await states.deal.sum.set()
#
#
# @F.message(state=states.deal.sum)
# async def state(message: types.Message, state: FSMContext):
#     if message.text == 'Назад ↩':
#         await state.finish()
#         wait = await bot.send_message(message.chat.id, '<b>Секунду...</b>', parse_mode="html",
#                                       reply_markup=default.remove)
#         await wait.delete()
#
#         await bot.send_message(message.chat.id, await string.menu(), parse_mode="html",
#                                reply_markup=await inline.menu())
#
#     elif message.text.isalpha():
#         await bot.send_message(message.from_user.id, "<b>Вы ввели не правильное число! 🔄</b>")
#
#     elif "." in message.text or "," in message.text:
#         await bot.send_message(message.from_user.id, "<b>Введите целое число! 🔄</b>")
#
#     elif int(message.text) <= 1:
#         await bot.send_message(message.from_user.id, "<b>Сумма сделки слишком мала! 🔄</b>")
#
#     elif int(message.text) > await DB.select_sum_forDeal(message.from_user.id,
#                                                          await DB.select_currencyDeal(message.from_user.id)):
#         await bot.send_message(message.from_user.id, "<b>У вас не достаточно баланса для сделки! 🔄</b>")
#
#
#     else:
#         await state.finish()
#
#         await DB.updateSumDeal(message.from_user.id, message.text)
#
#         wait = await bot.send_message(message.chat.id, '<b>Секунду...</b>', parse_mode="html",
#                                       reply_markup=default.remove)
#         await wait.delete()
#
#         await bot.send_message(message.from_user.id,
#                                f"*💲 Вы уверены что хотите отправить сделку?*\n\n_Сума сделки: {message.text} {await DB.select_currencyDeal(message.from_user.id)}_\n_ID пользователя:_ `{await DB.select_user_id_forDeal(message.from_user.id)}`",
#                                reply_markup=await inline.sendDeal(), parse_mode="MarkdownV2")
#
#
# # Отправить сделку
# @dp.callback_query(F.data =="sendDeal")
# async def sendDeal(call: types.CallbackQuery):
#     await call.message.delete()
#     await DB.updateBalance(call.from_user.id, await DB.select_currencyDeal(call.from_user.id),
#                            await DB.selectSum(call.from_user.id,
#                                               await DB.select_currencyDeal(call.from_user.id)) - await DB.selectSumDeal(
#                                call.from_user.id))
#
#     await bot.send_message(call.from_user.id,
#                            f"*Сделка успешно отправлена ✅*\n_ID пользователя: `{await DB.select_user_id_forDeal(call.from_user.id)}`_\n\n_Спасибо, что пользуетесь нашим ботом, для нас это очень важно\!😊_",
#                            reply_markup=await inline.back(), parse_mode="MarkdownV2")
#
#     user = await bot.get_chat(call.from_user.id)
#
#     if user.username:
#         name = "@" + user.username
#     else:
#         name = user.last_name + " " + user.first_name
#
#     deal_id = randint(10001, 99990)
#
#     await DB.addDeal(deal_id)
#     await DB.updateDeal(deal_id, call.from_user.id, await DB.select_user_id_forDeal(call.from_user.id),
#                         await DB.selectSumDeal(call.from_user.id), await DB.select_currencyDeal(call.from_user.id))
#
#     await bot.send_message(await DB.select_user_id_forDeal(call.from_user.id),
#                            f"*💸На ваш аккаунт поступила новая сделка от _{name}_*\n\n*💲Сума сделки:* _{await DB.selectSumDeal(call.from_user.id)} {await DB.select_currencyDeal(call.from_user.id)}_\n\n_Спасибо, что пользуетесь нашим ботом, для нас это очень важно\!😊_",
#                            reply_markup=await inline.back(), parse_mode="MarkdownV2")
