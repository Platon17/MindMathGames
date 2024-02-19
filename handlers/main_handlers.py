# Хэндлеры главного меню
from var import user_dict, cutting_dict, chet_dict, tickets_dict
from data import FSM_state, idPlaton
from services.services import _text,_txt,_atext,_set,_get, _load_user_dict
from keyboards.keyboards import create_inline_kb, create_kb, create_kb_ru
import json
from aiogram import Router
from aiogram.fsm.context import FSMContext


from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from handlers import sm_handlers

async def load_dict(redis,str_dict):
    json_dict = await redis.get(str_dict)
    if json_dict:
        return json.loads(json_dict)
    else:
        return {}

from aiogram.fsm.state import default_state, State, StatesGroup

# Инициализируем роутер уровня модуля
router_main = Router()
#router_main.message.filter(StateFilter(default_state))     # фильтрация
router_main.include_router(sm_handlers.router_sm)     # роутер решать

# выбор языка
@router_main.message(F.text.endswith('зык' ))
@router_main.message(F.text.endswith('anguage'))
@router_main.message(F.text=='🇷🇺 Язык 🇬🇧')
@router_main.message(F.text=='🇷🇺 Language 🇬🇧')
async def to_lang(message: types.Message, state: FSMContext):
    await message.answer(
            text=markdown.text(
                _text('what_lang4', 'ru')+"\n"+_text('what_lang4', 'en'),
                sep="\n"
            ),
            reply_markup=create_kb_ru(4, 'btnRU', 'btnEN', 'btnDE', 'btnCH')
        )
    await state.set_state(FSM_state.wLang)

@router_main.message(StateFilter(FSM_state.wLang), F.text=='🇷🇺 Русский')
#@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('усский'))
#@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('ussian'))
@router_main.message(F.text.endswith('усский'))
@router_main.message(F.text.endswith('ussian'))
async def set_lang_ru(message: types.Message, state: FSMContext):

    user_dict[str(message.from_user.id)] = {'lang': 'ru'}
#    await redis.set('user_dict', json.dumps(user_dict))
    await mm(message,state)

@router_main.message(StateFilter(FSM_state.wLang), F.text=='🇬🇧English')
#@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('нглийский'))
#@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('nglish'))
@router_main.message(F.text.endswith('nglish'))
@router_main.message(F.text.endswith('нглийский'))
async def set_lang_en(message: types.Message, state: FSMContext):
    user_dict[str(message.from_user.id)] = {'lang': 'en'}
#    await redis.set('user_dict', json.dumps(user_dict))
    await mm(message,state)

# знакомый язык, но без словаря
@router_main.message(StateFilter(FSM_state.wLang), F.text=='🇩🇪Deutsche')
#@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('eutsche'))
#@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('емецкий'))
@router_main.message(F.text.endswith('eutsche'))
@router_main.message(F.text.endswith('емецкий'))
async def set_lang_de(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('lang_known',message.from_user.id))
# незнакомый
@router_main.message(StateFilter(FSM_state.wLang))
async def set_lang_ch(message: types.Message, state: FSMContext):
    await message.answer(text=_text('lang_unknown', 'ru') + _text('lang_unknown', 'en'))
    await message.answer(text=_text('what_lang4', 'ru') + _text('what_lang4', 'en'))


@router_main.message(F.text=='🏘 Домой')
@router_main.message(F.text=='🏘 Home')
@router_main.message(F.text.endswith('омой'))
@router_main.message(F.text.endswith('home'))
@router_main.message(F.text.endswith('ancel'))
@router_main.message(F.text.endswith('тмена'))
async def mm(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('quote100', message.from_user.id))
    await message.answer(
        text=markdown.text(_txt('about1', message.from_user.id),sep="\n"),
        reply_markup=create_kb(4,message.from_user.id, 'btn_solve', 'btn_train', 'btn_research', 'btn_play', 'btn_speak','btn_AI','btn_language')
    )
    await state.clear()

@router_main.message(F.text=='⬅️ Назад', StateFilter(FSM_state.wSolve))
@router_main.message(F.text=='⬅️ Back', StateFilter(FSM_state.wSolve))
@router_main.message(F.text=='⬅️ Назад', StateFilter(FSM_state.wTrain))
@router_main.message(F.text=='⬅️ Back', StateFilter(FSM_state.wTrain))
@router_main.message(F.text=='⬅️ Назад', StateFilter(FSM_state.wReserch))
@router_main.message(F.text=='⬅️ Back', StateFilter(FSM_state.wReserch))
@router_main.message(F.text=='⬅️ Назад', StateFilter(FSM_state.wAI))
@router_main.message(F.text=='⬅️ Back', StateFilter(FSM_state.wAI))
@router_main.message(F.text=='⬅️ Назад', StateFilter(FSM_state.wSpeak))
@router_main.message(F.text=='⬅️ Back', StateFilter(FSM_state.wSpeak))
async def back_mm(message: types.Message, state: FSMContext):
    await mm(message, state)

# СТАРТ
@router_main.message(Command('start'))
@router_main.message(Command('cancel'))
@router_main.message(Command('home'))
@router_main.message(F.text.endswith('tart'))
@router_main.message(F.text.endswith('ачало'))
async def start(message: types.Message, state: FSMContext):
#    user_dict = await load_dict(redis, 'user_dict')
#    cutting_dict = await load_dict(redis, 'cutting_dict')
#    chet_dict = await load_dict(redis, 'chet_dict')
#    tickets_dict = await load_dict(redis, 'tickets_dict')
    # если пользователь впервые, спросим язык
    if str(message.from_user.id) not in user_dict:
        await message.answer(text=_text('hello3', 'ru')+"\n"+_text('hello3', 'en'))
        await to_lang(message, state)
    else:
        await message.answer(text=_txt('hello_again2', message.from_user.id))
        await mm(message, state)