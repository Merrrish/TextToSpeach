from aiogram import Bot, Dispatcher
import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv
from App.handlers import router

# Загружаем переменные из .env
load_dotenv()

# Получаем токен из переменных окружения
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    print(f"Время запуска кода: {datetime.now()}")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"Программа была завершена: {datetime.now()}")
