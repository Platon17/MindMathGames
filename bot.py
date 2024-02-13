
import asyncio
import logging
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, Game

from aiogram import Bot, F
from aiogram import Dispatcher
from handlers import main_handlers

from data import FSM_state, idPlaton


from aiogram.filters import BaseFilter # для создания своих фильтров
from aiogram.filters import Command, StateFilter, or_f
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from bilet import bilet
import config
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# from handlers import mm_handlers

# base logic
from services.services import _text
from services.cutting import cut, m_to_str
from services.tickets import solve as ticketsolve, numbers_opers
from services.best_path import find_path

# === FSM ===
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
config = config.load_config()
BOT_TOKEN: str = config.tg_bot.token
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
async def start_bot(bot: Bot):
    await bot.send_message(idPlaton, text="Бот запущен!")
async def stop_bot(bot: Bot):
    await bot.send_message(idPlaton, text="Бот остановлен!")
async def main():
    #
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode=ParseMode.HTML,
    )
    # dp.startup.register(start_bot)     # отправить сообщение о включении бота
    # dp.shutdown.register(stop_bot)     # отправить сообщение о выключение бота
    # Регистриуем роутеры в диспетчере
    dp.include_router(main_handlers.router_main)  # роутеры главного меню
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())