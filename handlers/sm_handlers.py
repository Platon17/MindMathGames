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
router_sm = Router()
#router_sm.message.filter(StateFilter(default_state)) # фильтрация
router_sm.include_router(artur_handlers.router_artur)        # ДЕЛЁЖ КОРОЛЯ АРТУРА
router_sm.include_router(tickets_handlers.router_tickets)    # БИЛЕТЫ
router_sm.include_router(simm_handlers.router_simm)          # СИММЕТРИЯ
router_sm.include_router(cutting_handlers.router_cutting)    # РАЗРЕЗАНИЕ
router_sm.include_router(chet_handlers.router_chet)          # ЧЕТНО-НЕЧЕТНО
router_sm.include_router(path_handlers.router_path)          # ЛУЧШИЙ ПУТЬ

# РЕШАТЬ
@router_sm.message(Command('solve'))
@router_sm.message(F.text=='🧩️ Решать')
@router_sm.message(F.text=='🧩️ Solve')
@router_sm.message(F.text.endswith('ешать'))
@router_sm.message(F.text.endswith('ешать'))
@router_sm.message(F.text.startwith('Реши'))
@router_sm.message(F.text.startwith('реши'))
@router_sm.message(F.text.startwith('Найди'))
@router_sm.message(F.text.startwith('найди'))
@router_sm.message(F.text.endswith('Solve'))
@router_sm.message(F.text.endswith('solve'))
async def solve(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('quote100', message.from_user.id))
    await message.answer(
        text=markdown.text(_txt('solve_about', message.from_user.id),sep="\n"),
        reply_markup=create_kb(4,message.from_user.id, 'btn_back', 'btn_home', 'btn_tickets', 'btn_cutting','btn_path', 'btn_simm', 'btn_chet','btn_add')
    )
    await state.set_state(FSM_state.wSolve)

# ИССЛЕДОВАТЬ
@router_sm.message(Command('research'))
@router_sm.message(F.text=='🧑‍🔬 Исследовать')
@router_sm.message(F.text=='🧑‍🔬 Research')
@router_sm.message(F.text.endswith('сследовать'))
@router_sm.message(F.text.startwith('Исследовать'))
@router_sm.message(F.text.startwith('исследовать'))
@router_sm.message(F.text.endswith('esearch'))
@router_sm.message(F.text.startwith('Research'))
@router_sm.message(F.text.startwith('research'))
async def research(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('quote100', message.from_user.id))
    await message.answer(
        text=markdown.text(_txt('research_about', message.from_user.id),sep="\n"),
        reply_markup=create_kb(4,message.from_user.id, 'btn_back', 'btn_home', 'btn_artur', 'btn_add')
    )
    await state.set_state(FSM_state.wReserch)

@router_sm.message(Command('train'))
@router_sm.message(F.text=='🧠 Тренироваться')
@router_sm.message(F.text=='🧠 Train')
@router_sm.message(F.text.endswith('ренироваться'))
@router_sm.message(F.text.startwith('Задай'))
@router_sm.message(F.text.startwith('задай'))
@router_sm.message(F.text.startwith('Спроси'))
@router_sm.message(F.text.startwith('спроси'))
@router_sm.message(F.text.endswith('Train'))
@router_sm.message(F.text.endswith('train'))
async def train(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('quote100', message.from_user.id))
    await message.answer(
        text=markdown.text(_txt('train_about', message.from_user.id), sep="\n"),
        reply_markup=create_kb(4, message.from_user.id, 'btn_back', 'btn_home', 'btn_tickets', 'btn_cutting','btn_path', 'btn_simm', 'btn_chet', 'btn_add')
    )
    await state.set_state(FSM_state.wTrain)

@router_sm.message(Command('play'))
@router_sm.message(F.text=='🎲 Играть')
@router_sm.message(F.text=='🎲 Play')
@router_sm.message(F.text.endswith('рать'))
@router_sm.message(F.text.startwith('Игра'))
@router_sm.message(F.text.startwith('игра'))
@router_sm.message(F.text.startwith('Play'))
@router_sm.message(F.text.startwith('play'))
@router_sm.message(F.text.endswith('Play'))
@router_sm.message(F.text.endswith('play'))
async def train(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('quote100', message.from_user.id))
    await message.answer(
        text=markdown.text(_txt('train_about', message.from_user.id), sep="\n"),
        reply_markup=create_kb(4, message.from_user.id, 'btn_back', 'btn_home', 'btn_tickets', 'btn_cutting','btn_path', 'btn_simm', 'btn_chet', 'btn_add')
    )
    await state.set_state(FSM_state.wTrain)
@router_sm.message(Command('ai'))
@router_sm.message(F.text.endswith('интеллект'))
@router_sm.message(F.text.startwith('Искусственный интеллект'))
@router_sm.message(F.text.startwith('Искусственный интеллект'))
async def AI(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('quote100', message.from_user.id))
    await message.answer(
        text=markdown.text(_txt('AI_about', message.from_user.id), sep="\n"),
        reply_markup=create_kb(4, message.from_user.id, 'btn_back', 'btn_home', 'ChatGPT', 'CharacterAI', 'GoogleBard', 'JanitorAI',
                               'PerplexityAI', 'Civitai', 'LeonardoAI', 'ElevenLabs', 'CapCut', 'Cutout.pro')

    )
    await state.set_state(FSM_state.wAI)

@router_sm.message(Command('speak'))
@router_sm.message(F.text.endswith('оговорим'))
@router_sm.message(F.text.endswith('оговорить'))
@router_sm.message(F.text.startwith('Расскажи'))
@router_sm.message(F.text.startwith('расскажи'))
@router_sm.message(F.text.startwith('Поговори'))
@router_sm.message(F.text.startwith('поговори'))
async def speak(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('quote100', message.from_user.id))
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

@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wArtur))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wCutting))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wPath))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wTicket))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wChet))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wSimm))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wArtur))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wCutting))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wPath))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wTicket))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wChet))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wSimm))
async def back_to_slove(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wSolve)
    await solve(message, state)


@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wArtur))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wAnsChet))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wAnsSimm))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wAnsTicket))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wAnsCutting))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wAnsPath))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wArtur))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wAnsChet))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wAnsSimm))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wAnsTicket))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wAnsCutting))
@router_sm.message(F.text == '⬅️ Back', StateFilter(FSM_state.wAnsPath))
async def back_to_train(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wTrain)
    await train(message, state)

@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wArtur))
@router_sm.message(F.text == '⬅️ Назад', StateFilter(FSM_state.wArturCoin))
async def back_to_research(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wTrain)
    await research(message, state)
