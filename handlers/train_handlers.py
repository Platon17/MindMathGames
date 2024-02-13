# Хэндлеры главного меню
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import types
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext


import asyncio
import logging
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, Game
from aiogram import Bot, F
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from bilet import bilet
import config

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from FindPath import find_path
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram.fsm.state import default_state, State, StatesGroup
from handlers import solve_tiсkets_handlers
from services.services import _text

class FSM_state(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    choise_lang = State()   # Состояние ожидания выбора языка
    fill_name = State()     # Состояние ожидания ввода имени
    choise_action = State() # Состояние ожидания выбора действия
    choise_task = State()   # Состояние ожидания выбора задачи
    Task1 = State()  # Состояние ожидания выбора задачи

# Инициализируем роутер уровня модуля
routerT1 = Router()
routerT1.message.filter(StateFilter(FSM_state.Task1))
#routerS.include_router(solve_tiсkets_handlers.router)   # роутеры решать