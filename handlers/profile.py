from utils import string
from aiogram.fsm.context import FSMContext
from database import DB
from aiogram import types, F
from keyboards import inline, default
from loader import dp, bot, form_router
import config
from state import states
from aiocryptopay import AioCryptoPay, Networks



@dp.message(F.text == '🎓 Профиль')
async def profile(message: types.Message):
    user_id = message.from_user.id
    file = await bot.get_user_profile_photos(user_id=message.from_user.id)
    try:
        photo = await bot.get_file(file.photos[-1][-1].file_id)
        await bot.send_photo(message.from_user.id, photo.file_id, caption=f'🎖 <b>Мой профиль: @{message.from_user.username}</b>\n\n' 
                                                                          f'<b>👤 Имя [</b><code>{user_id}</code><b>]:</b> <code>{message.from_user.first_name}</code>\n'
                                                                          f'<b>👨‍💻 Статус:</b>\n'
                                                                          f'<b>🏆 Рейтинг:</b>\n\n'
                                                                          f'<b>💳 Депозит:</b>\n\n'
                                                                          f'<b>🛒 Покупок:</b>\n'
                                                                          f'<b>💼 Продаж:</b>', parse_mode="HTML")

    except IndexError:
        await bot.send_message(message.from_user.id, text=f'🎖 <b>Мой профиль: @{message.from_user.username}</b>\n\n'
                                                          f'<b>👤 Имя [</b><code>{user_id}</code><b>]:</b> <code>{message.from_user.first_name}</code>\n'
                                                          f'<b>👨‍💻 Статус:</b>\n'
                                                          f'<b>🏆 Рейтинг:</b>\n\n'
                                                          f'<b>💳 Депозит:</b>\n\n'
                                                          f'<b>🛒 Покупок:</b>\n'
                                                          f'<b>💼 Продаж:</b>', parse_mode="HTML")


# Профиль
# @dp.callback_query(F.data == "profile")
# async def profile(call: types.CallbackQuery):
#     await call.message.delete()
#     user_id = call.from_user.id
#
#     file = await bot.get_user_profile_photos(user_id=call.from_user.id)
#
#     try:
#         photo = await bot.get_file(file.photos[-1][-1].file_id)
#
#         await bot.send_photo(call.message.chat.id, photo.file_id,
#                              caption=await string.profile(user_id, await DB.selectName(user_id),
#                                                           await DB.selectTON(user_id),
#                                                           await DB.selectUSDT(user_id),
#                                                           await DB.selectBUSD(user_id), await DB.selectUSDC(user_id),
#                                                           await DB.selectQuantitySell(user_id),
#                                                           await DB.selectQuantityBuy(user_id),
#                                                           await DB.selectSellUSD(user_id),
#                                                           await DB.selectBuyUSD(user_id)),
#                              reply_markup=await inline.profile(), parse_mode="MarkdownV2")
#     except IndexError:
#         await bot.send_message(call.from_user.id, text=await string.profile(user_id, await DB.selectName(user_id),
#                                                                             await DB.selectTON(user_id),
#                                                                             await DB.selectUSDT(user_id),
#                                                                             await DB.selectBUSD(user_id),
#                                                                             await DB.selectUSDC(user_id),
#                                                                             await DB.selectQuantitySell(user_id),
#                                                                             await DB.selectQuantityBuy(user_id),
#                                                                             await DB.selectSellUSD(user_id),
#                                                                             await DB.selectBuyUSD(user_id)),
#                                parse_mode="MarkdownV2", reply_markup=await inline.profile())
#
#
# # Пополнение баланса
# @dp.callback_query(F.data == "deposit")
# async def deposit(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.from_user.id, f"<b>Выберите способ оплаты криптовалютой! 💎</b>", parse_mode="html",
#                            reply_markup=await inline.crypto())
#
#
# # Выбор криптовалюты для пополнения
# @dp.callback_query(F.data == ["TON", "USDT", "BUSD", "USDC"])
# async def crypto(call: types.CallbackQuery):
#     await call.message.delete()
#     await DB.updateCrypto(call.from_user.id, call.data)
#
#     await bot.send_message(call.from_user.id, f"<b>💰 Введите сумму пополнения в ({call.data}) !</b>", parse_mode="html",
#                            reply_markup=await default.back())
#
#     await states.deposit.sum.set()
#
#
# @form_router.message(states.deposit.sum)
# async def state(message: types.Message, state: FSMContext):
#     if message.text == 'Назад ↩':
#         await state.finish()
#         await bot.send_message(message.chat.id, '<b>Секунду...</b>', parse_mode="html", reply_markup=default.remove)
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
#
#     elif message.text == "0":
#         await bot.send_message(message.from_user.id, "<b>Число '<1' не может быть суммой пополнения! 🔄</b>")
#
#     else:
#         await state.finish()
#
#         await DB.updateSumPaid(message.from_user.id, message.text)
#
#         wait = await bot.send_message(message.chat.id, '<b>Секунду...</b>', parse_mode="html",
#                                       reply_markup=default.remove)
#         await wait.delete()
#
#         await bot.send_message(message.from_user.id, "<b>Вы уверены что хотите пополнить баланс?</b>",
#                                reply_markup=await inline.assured())
#
#
# # Уверен что хочу оплатить/Оплатил
# @dp.callback_query(F.data ==["assured", "paid"])
# async def assured(call: types.CallbackQuery):
#     crypto = AioCryptoPay(token=config.cryptoTOKEN, network=Networks.MAIN_NET)
#
#     if call.data == "assured":
#         try:
#             await call.message.delete()
#             invoice = await crypto.create_invoice(asset=await DB.selectCrypto(call.from_user.id),
#                                                   amount=int(await DB.selectSumPaid(call.from_user.id)))
#
#             await DB.updateInvoiceId(call.from_user.id, invoice.invoice_id)
#             await DB.updateInvoiceUrl(call.from_user.id, invoice.pay_url)
#
#             await bot.send_message(call.message.chat.id, invoice.pay_url, reply_markup=await inline.check())
#         except:
#             await bot.send_message(call.message.chat.id,
#                                    '<b>Вы ввели неправильное значение, или сумма слишком мала! Попробуйте снова!</b>',
#                                    parse_mode="html", reply_markup=await inline.crypto())
#
#     else:
#         await call.message.delete()
#         invoices = await crypto.get_invoices(invoice_ids=await DB.selectInvoiceId(call.from_user.id))
#
#         if str(invoices.status) == "InvoiceStatus.PAID":
#             if await DB.selectCrypto(call.from_user.id) == "TON":
#                 await DB.updateTON(call.from_user.id,
#                                    await DB.selectTON(call.from_user.id) + await DB.selectSumPaid(call.from_user.id))
#
#             elif await DB.selectCrypto(call.from_user.id) == "USDT":
#                 await DB.updateUSDT(call.from_user.id,
#                                     await DB.selectUSDT(call.from_user.id) + await DB.selectSumPaid(call.from_user.id))
#
#             elif await DB.selectCrypto(call.from_user.id) == "BUSD":
#                 await DB.updateBUSD(call.from_user.id,
#                                     await DB.selectBUSD(call.from_user.id) + await DB.selectSumPaid(call.from_user.id))
#
#             elif await DB.selectCrypto(call.from_user.id) == "USDC":
#                 await DB.updateUSDC(call.from_user.id,
#                                     await DB.selectUSDC(call.from_user.id) + await DB.selectSumPaid(call.from_user.id))
#
#             await bot.send_message(call.from_user.id, "<b> Отлично, ваш баланс пополнено! ✅ </b>",
#                                    reply_markup=await inline.back())
#
#         else:
#             await bot.send_message(call.from_user.id,
#                                    f"<b>Вы еще не совершили оплату!</b>\nСсылка на оплату: {await DB.selectInvoiceUrl(call.from_user.id)}",
#                                    reply_markup=await inline.check())
#
#
# # Вывод баланса
# @dp.callback_query(F.data == "withdraw")
# async def withdraw(call: types.CallbackQuery):
#     await call.message.delete()
#     await bot.send_message(call.from_user.id,
#                            f"🔹_ID аккаунта:_ `{call.from_user.id}`\n\n☺️ℹ️ *Свяжитесь с админом для вывода средств\!\nПредварительно отправте ему ваш _ID аккаунта_\!*",
#                            parse_mode="MarkdownV2",
#                            reply_markup=await inline.withdraw())
