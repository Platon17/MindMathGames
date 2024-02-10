# Хэндлеры главного меню
from var import user_dict
from data import FSM_state, max_variants
from filters.tickets_filters import WordTicket, WordSolveTicket, WordGiveUp, WordExamplTicket, WordTrainTicket, RightTicket, RightOpers
from filters.main_filters import strDict, WordExampl, WordOptions
from services.services import _txt


from aiogram import Router
from aiogram.fsm.context import FSMContext


from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from handlers import tickets_handlers

# Инициализируем роутер уровня модуля
router_path = Router()


#@router_path.message(message.text == _txt('path'))
@router_path.message(F.text.startwith('path'))
async def path(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wPath)
    kb = [
        [
            types.KeyboardButton(text=_txt('back')),
            types.KeyboardButton(text=_txt('home')),
            types.KeyboardButton(text=_txt('examples')),
            types.KeyboardButton(text=_txt('message.from_user.id')),
            types.KeyboardButton(text=_txt('options')),
        ]
    ]


    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_txt('txt_solve_path')
    )
    await message.answer(
        text=markdown.text(
            _txt('txt_solve_path'),
            markdown.text(_txt('input_path'),
                          ),
            sep="\n"
        ),
        reply_markup=keyboard
    )