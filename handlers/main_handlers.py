# Хэндлеры главного меню
from var import user_dict
from data import FSM_state, idPlaton
from services.services import _text,_txt,_atext
from keyboards.keyboards import create_inline_kb, create_kb, create_kb_ru

from aiogram import Router
from aiogram.fsm.context import FSMContext


from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from handlers import solve_handlers



from aiogram.fsm.state import default_state, State, StatesGroup


# Инициализируем роутер уровня модуля
router_main = Router()
#router_main.message.filter(StateFilter(default_state))     # фильтрация
router_main.include_router(solve_handlers.router_solve)     # роутер решать

# выбор языка
@router_main.message(F.text.endswith('зык' ))
@router_main.message(F.text.endswith('anguage'))
@router_main.message(F.text=='🇷🇺 Язык 🇬🇧')
async def to_lang(message: types.Message, state: FSMContext):
    await message.answer(
            text=markdown.text(
                _text('what_lang4', 'ru')+_text('what_lang4', 'en'),
                sep="\n"
            ),
            reply_markup=create_kb_ru(3, 'btnRU', 'btnEN', 'btnDE', 'btnCH','btnJP')
        )
    await state.set_state(FSM_state.wLang)

@router_main.message(F.text=='🏘 Домой')
@router_main.message(F.text=='🏘 Home')
@router_main.message(F.text.endswith('омой'))
@router_main.message(F.text.endswith('home'))
@router_main.message(F.text.endswith('ancel'))
@router_main.message(F.text.endswith('тмена'))
async def mm(message: types.Message, state: FSMContext):
        await message.answer(
            text=markdown.text(
                _txt('about1', message.from_user.id),
                sep="\n"
            ),
            reply_markup=create_kb(3,message.from_user.id, 'btn_solve', 'btn_train', 'btn_research', 'btn_speak','btn_AI','btn_language')
        )
        await message.answer(text=_txt('about1', message.from_user.id))
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
# команда СТАРТ
@router_main.message(Command('start'))
@router_main.message(Command('cancel'))
@router_main.message(Command('home'))
@router_main.message(F.text.endswith('tart'))
@router_main.message(F.text.endswith('ачало'))
async def start(message: types.Message, state: FSMContext):
    # если пользователь впервые, спросим язык
    if message.from_user.id not in user_dict:
        await message.answer(text=_text('Hello1', 'ru'))
        await to_lang(message, state)
    else:
        await message.answer(text=_txt('hello_again', message.from_user.id))
        await mm(message, state)

@router_main.message(StateFilter(FSM_state.wLang), F.text=='🇷🇺 Русский')
@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('усский'))
@router_main.message(F.text.endswith('усский'))
async def set_lang_ru(message: types.Message, state: FSMContext):
    user_dict[message.from_user.id] = {'lang': 'ru'}
    await mm(message,state)

@router_main.message(StateFilter(FSM_state.wLang), F.text=='🇬🇧English')
@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('nglish'))
@router_main.message(F.text.endswith('nglish'))
async def set_lang_en(message: types.Message, state: FSMContext):
    user_dict[message.from_user.id] = {'lang': 'en'}
    await mm(message,state)

# знакомый язык, но без словаря
@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('eutsche'))
@router_main.message(F.text.endswith('eutsche'))
async def set_lang_de(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('lang_known',message.from_user.id))
# незнакомый
@router_main.message(StateFilter(FSM_state.wLang))
async def set_lang_ch(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('lang_unknown',message.from_user.id))
## Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
@router_main.message(Command('cancel'))
async def process_cancel_command_state(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('lets_do', message.from_user.id))
    await state.clear()

@router_main.message(Command('hello'))
async def hello(message: types.Message):
    url = "https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg"
    await message.answer(
        text=_text('Hello2'),
        parse_mode=ParseMode.HTML
    )