# Хэндлеры главного меню
from aiogram import Router
from aiogram.fsm.context import FSMContext

from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.utils import markdown

from aiogram.fsm.state import default_state, State, StatesGroup
from services.services import _text
from handlers import sm_handlers

class FSM_state(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    mm = State()
    sm = State()
    wStrTickets = State()
    wResult = State()
    wAll = State()

# Инициализируем роутер уровня модуля
router_mm = Router()
#router.message.filter(StateFilter(default_state))
router_mm.include_router(sm_handlers.router_sm)   # роутеры решать


# ГЛАВНОЕ МЕНЮ
# срабатывает всегда если сброшено состояние
#@router_mm.message(StateFilter(default_state))
@router_mm.message(or_f(
    StateFilter(default_state),
            F.text == _text('home'),
            F.text == _text('back')
))
async def toMainMenu(message: types.Message, state: FSMContext):
    global lang
    lang = 'ru'
    if message.text == _text('langEN'): lang = 'en'

    kb = [
        [
            types.KeyboardButton(text=_text('solve',lang)),
            types.KeyboardButton(text=_text('reserch',lang)),
            types.KeyboardButton(text=_text('train',lang)),
#            types.KeyboardButton(text=_text('speak',lang)),
#            types.KeyboardButton(text=_text('AI'),lang),
            types.KeyboardButton(text=_text('Options',lang)),

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_text('choice_actions',lang)
    )
    await message.answer(
        text=markdown.text(
            _text('mm',lang),
            markdown.text(_text('choice_actions',lang),
            ),
            sep="\n"
        ),
        reply_markup=keyboard
    )
    await state.update_data(lan=message.text.lower())
    await state.set_state(FSM_state.mm)
    await message.answer('Стало состояние mm')
    await message.answer(lang)