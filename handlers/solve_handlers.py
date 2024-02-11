# Хэндлеры главного меню
from var import user_dict
from data import FSM_state
from services.services import _txt

from aiogram import Router
from aiogram.fsm.context import FSMContext


from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.utils import markdown
from keyboards.keyboards import create_inline_kb, create_kb, create_kb_ru
from aiogram.enums import ParseMode
from handlers import tickets_handlers, cutting_handlers, path_handlers, simm_handlers, chet_handlers, artur_handlers

# Инициализируем роутер уровня модуля
router_solve = Router()
#router_solve.message.filter(StateFilter(default_state)) # фильтрация
router_solve.include_router(tickets_handlers.router_tickets)   # БИЛЕТЫ
router_solve.include_router(cutting_handlers.router_cutting)   # РАЗРЕЗАНИЕ
router_solve.include_router(path_handlers.router_path)          # ЛУЧШИЙ ПУТЬ
router_solve.include_router(simm_handlers.router_simm)          # СИММЕТРИЯ
router_solve.include_router(chet_handlers.router_chet)          # ЧЕТНО-НЕЧЕТНО
router_solve.include_router(artur_handlers.router_artur)         # ДЕЛЁЖ КОРОЛЯ АРТУРА

# РЕШАТЬ
@router_solve.message(Command('solve'))
@router_solve.message(F.text.endswith('ешать'))
@router_solve.message(F.text.startwith('Реши'))
@router_solve.message(F.text.startwith('реши'))
@router_solve.message(F.text.startwith('Найди'))
@router_solve.message(F.text.startwith('найди'))
async def solve(message: types.Message, state: FSMContext):
    await message.answer(
        text=markdown.text(_txt('solve_about', message.from_user.id),sep="\n"),
        reply_markup=create_kb(4,message.from_user.id, 'btn_back', 'btn_home', 'btn_tickets', 'btn_cutting','btn_path','btn_simm','btn_chet','btn_add')
    )
    await state.set_state(FSM_state.wSolve)

# ИССЛЕДОВАТЬ
@router_solve.message(Command('research'))
@router_solve.message(F.text.endswith('сследовать'))
@router_solve.message(F.text.startwith('Исследовать'))
@router_solve.message(F.text.startwith('исследовать'))
@router_solve.message(F.text.endswith('esearch'))
@router_solve.message(F.text.startwith('Research'))
@router_solve.message(F.text.startwith('research'))
async def research(message: types.Message, state: FSMContext):
    await message.answer(
        text=markdown.text(_txt('research_about', message.from_user.id),sep="\n"),
        reply_markup=create_kb(4,message.from_user.id, 'btn_back', 'btn_home', 'btn_artur', 'btn_add')
    )
    await state.set_state(FSM_state.wReserch)

@router_solve.message(Command('train'))
@router_solve.message(F.text.endswith('ренироваться'))
@router_solve.message(F.text.startwith('Задай'))
@router_solve.message(F.text.startwith('задай'))
@router_solve.message(F.text.startwith('Спроси'))
@router_solve.message(F.text.startwith('спроси'))
async def train(message: types.Message, state: FSMContext):
    await message.answer(
        text=markdown.text(_txt('train_about', message.from_user.id), sep="\n"),
        reply_markup=create_kb(4, message.from_user.id, 'btn_back', 'btn_home', 'btn_tickets', 'btn_cutting','btn_path', 'btn_simm', 'btn_chet', 'btn_add')
    )
    await state.set_state(FSM_state.wTrain)

@router_solve.message(Command('ai'))
@router_solve.message(F.text.endswith('интеллект'))
@router_solve.message(F.text.startwith('Искусственный интеллект'))
@router_solve.message(F.text.startwith('Искусственный интеллект'))
async def AI(message: types.Message, state: FSMContext):
    await message.answer(
        text=markdown.text(_txt('AI_about', message.from_user.id), sep="\n"),
        reply_markup=create_kb(4, message.from_user.id, 'btn_back', 'btn_home', 'ChatGPT', 'CharacterAI', 'GoogleBard', 'JanitorAI',
                               'PerplexityAI', 'Civitai', 'LeonardoAI', 'ElevenLabs', 'CapCut', 'Cutout.pro')

    )
    await state.set_state(FSM_state.wAI)

@router_solve.message(Command('speak'))
@router_solve.message(F.text.endswith('оговорим'))
@router_solve.message(F.text.endswith('оговорить'))
@router_solve.message(F.text.startwith('Расскажи'))
@router_solve.message(F.text.startwith('расскажи'))
@router_solve.message(F.text.startwith('Поговори'))
@router_solve.message(F.text.startwith('поговори'))
async def AI(message: types.Message, state: FSMContext):
    kb = [
        [
            types.KeyboardButton(text=_txt('quotes', message.from_user.id)),
            types.KeyboardButton(text=_txt('jokes', message.from_user.id)),
            types.KeyboardButton(text=_txt('sport', message.from_user.id)),
            types.KeyboardButton(text=_txt('politic', message.from_user.id)),
            types.KeyboardButton(text=_txt('computers', message.from_user.id)),
        ],
        [
            types.KeyboardButton(text=_txt('AI', message.from_user.id)),
            types.KeyboardButton(text=_txt('avto', message.from_user.id)),
            types.KeyboardButton(text=_txt('music', message.from_user.id)),
            types.KeyboardButton(text=_txt('video', message.from_user.id)),
            types.KeyboardButton(text=_txt('weather', message.from_user.id)),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(
        text=markdown.text(_txt('speak_about', message.from_user.id), sep="\n"),
        reply_markup=create_kb(4, message.from_user.id, 'btn_back', 'btn_home', 'btn_quotes', 'btn_jokes', 'btn_sport', 'btn_politic', 'btn_computers', 'btn_weather','btn_music', 'btn_video', 'btn_avto', 'btn_AI')
    )
    await state.set_state(FSM_state.wSpeak)
    @router_solve.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wCutting))
    @router_solve.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wPath))
    @router_solve.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wTicket))
    async def back_mm(message: types.Message, state: FSMContext):
        await solve(message, state)
        await state.set_state(FSM_state.wSolve)

        #                          | (F.text == '⬅️ Back'), (StateFilter(FSM_state.wCutting) | StateFilter(FSM_state.wPath) | StateFilter(FSM_state.wTicket)))