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
from handlers import train_handlers
from services.services import _text

class FSM_state(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    choise_lang = State()   # Состояние ожидания выбора языка
    fill_name = State()     # Состояние ожидания ввода имени
    choise_action = State() # Состояние ожидания выбора действия
    choise_task = State()   # Состояние ожидания выбора задачи

# Инициализируем роутер уровня модуля
routerT = Router()
routerT.message.filter(StateFilter(FSM_state.choise_task))
routerT.include_router(train_handlers.routerT1)   # роутеры решать

# ГЛАВНОЕ МЕНЮ
# сотояние должно быть default
@routerT.message(StateFilter(FSM_state.choise_task),F.text == _text('tickets'))
async def toMainMenu(message: types.Message, state: FSMContext):
    await message.answer('Было состояние choise_action')
    kb = [
        [
            types.KeyboardButton(text=_text('tickets')),
#            types.KeyboardButton(text=_text('cutting')),
#            types.KeyboardButton(text=_text('simm')),
#            types.KeyboardButton(text=_text('chet')),
#            types.KeyboardButton(text=_text('path')),
#            types.KeyboardButton(text=_text('artur')),
            types.KeyboardButton(text=_text('back')),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_text('txt_solve')
    )
    await message.answer(
        text=markdown.text(
            _text('txt_solve'),
            markdown.text(_text('choice_tasks'),
            ),
            sep="\n"
        ),
        reply_markup=keyboard
    )
    await state.set_state(FSM_state.choise_task)
    await message.answer('Стало состояние choise_task' )

@routerT.message(StateFilter(FSM_state.choise_task),F.text == _text('back'))
async def mm(message: Message):
    await message.answer('Cостояние SOLVE' )
@routerT.message()
async def mm(message: Message):
    await message.answer('Cостояние SOLVE' )