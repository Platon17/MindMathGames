# Хэндлеры главного меню
from aiogram import Router
from aiogram.fsm.context import FSMContext


from aiogram import F
from aiogram import types
from aiogram.filters import StateFilter, or_f
from aiogram.utils import markdown

from aiogram.fsm.state import default_state, State, StatesGroup
from services.services import _text
from handlers import tasks_handlers

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
router_sm = Router()
router_sm.include_router(tasks_handlers.router_tasks)   # роутеры задач
#router_sm.include_router(tasks_handlers.router_reserch) # роутеры иссследований
#router_sm.include_router(tasks_handlers.router_train)   # роутеры тренировок
#router_sm.include_router(tasks_handlers.router_AI)      # роутеры ИИ


# ГЛАВНОЕ МЕНЮ
# срабатывает всегда если сброшено состояние
#@router.message(StateFilter(default_state))
@router_sm.message(StateFilter(FSM_state.mm))
async def solve(message: types.Message, state: FSMContext):
    kb = [
        [
            types.KeyboardButton(text=_text('tickets')),
            types.KeyboardButton(text=_text('cutting')),
            types.KeyboardButton(text=_text('simm')),
#            types.KeyboardButton(text=_text('speak')),
#            types.KeyboardButton(text=_text('AI')),
#            types.KeyboardButton(text=_text('Options')),

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_text('choise_tasks')
    )
    await message.answer(
        text=markdown.text(
            _text('txt_solve'),
            markdown.text(_text('choise_tasks'),
            ),
            sep="\n"
        ),
        reply_markup=keyboard
    )
    await state.set_state(FSM_state.sm)
    await message.answer('Стало состояние sm')
    userdata = await state.get_data()
    await message.answer(userdata['lan'])