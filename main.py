from aiogram import Bot, Dispatcher
import asyncio
from datetime import datetime
from App.config import TOKEN
from App.handlers import router


token = TOKEN
bot = Bot(token)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    print(f"Время запуска кода: {datetime.now()}")
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа была завершена: {datetime.now()}")