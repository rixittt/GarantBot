from aiogram import Bot, Dispatcher, F, Router
import config
import asyncio

bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher()
form_router = Router()

