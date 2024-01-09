import logging
from aiogram import Bot, Dispatcher, F
from handlers import dp
import asyncio
from loader import bot

logging.basicConfig(level=logging.INFO)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



# ████─ █ ▄▄▄▄███████████
# █▀██─ █▄▄▄▄ █ ▄ █ ▄ █ █
# ▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄█▄▄▄▀