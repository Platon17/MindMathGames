# Хэндлеры главного меню
from var import user_dict
from data import FSM_state, idPlaton
from services.services import _text,_txt,_atext

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

# СТАРТ
# команда СТАРТ
@router_main.message(Command('start'))
@router_main.message(Command('cancel'))
@router_main.message(Command('home'))
@router_main.message(F.text.endswith('tart'))
@router_main.message(F.text.endswith('ачало'))
@router_main.message(F.text.endswith('омой'))
@router_main.message(F.text.endswith('home'))
@router_main.message(F.text.endswith('ancel'))
@router_main.message(F.text.endswith('тмена'))
async def start(message: types.Message, state: FSMContext):

    # если пользователь впервые, спросим язык
    if message.from_user.id not in user_dict:
        kb = [[types.KeyboardButton(text=_text('btnRU')), types.KeyboardButton(text=_text('btnEN')),
               types.KeyboardButton(text=_text('btnDE')), types.KeyboardButton(text=_text('btnCH'))]]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder='btnRU'
        )
        await message.answer(
            text=markdown.text(_text('what_lang4','ru')+'\n'+_text('what_lang4','en')),
            reply_markup=keyboard
        )
        await state.set_state(FSM_state.wLang)
    else:
        kb = [
            [
                types.KeyboardButton(text=_txt('solve', message.from_user.id)),
                types.KeyboardButton(text=_txt('reserch', message.from_user.id)),
                types.KeyboardButton(text=_txt('train', message.from_user.id))
            ],
            [
                types.KeyboardButton(text=_txt('speak', message.from_user.id)),
                types.KeyboardButton(text=_txt('AI', message.from_user.id)),
                types.KeyboardButton(text=_txt('language', message.from_user.id)),

            ]
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True
        )
        await message.answer(
            text=markdown.text(
                _txt('hello_again', message.from_user.id),
                sep="\n"
            ),
            reply_markup=keyboard
        )

        await message.answer(text=_txt('about1', message.from_user.id))
        await state.clear()
# выбор языка
@router_main.message(F.text.endswith('зык' ))
@router_main.message(F.text.endswith('anguage'))
async def to_lang(message: types.Message, state: FSMContext):
    kb = [[types.KeyboardButton(text=_text('btnRU')), types.KeyboardButton(text=_text('btnEN')),
           types.KeyboardButton(text=_text('btnDE')), types.KeyboardButton(text=_text('btnCH'))]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_text('what_lang4', 'ru') + ' ' + _text('what_lang4', 'en')
    )
    await message.answer(
        text=markdown.text(_text('what_lang4', 'ru') + '\n' + _text('what_lang4', 'en'),sep="\n"),
        reply_markup=keyboard
    )
    await state.set_state(FSM_state.wLang)

@router_main.message(StateFilter(FSM_state.wLang),F.text.endswith('усский'))
@router_main.message(F.text.endswith('усский'))
async def set_lang(message: types.Message, state: FSMContext):
    user_dict[message.from_user.id] = {'lang': 'ru'}
    kb = [
        [
            types.KeyboardButton(text=_text('solve','ru')),
            types.KeyboardButton(text=_text('reserch', 'ru')),
            types.KeyboardButton(text=_text('train', 'ru'))
        ],
        [
            types.KeyboardButton(text=_text('speak', 'ru')),
            types.KeyboardButton(text=_text('AI', 'ru')),
            types.KeyboardButton(text=_text('Options', 'ru')),

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(
        text=markdown.text(
            _text('hello3','ru'),
            sep="\n"
        ),
        reply_markup=keyboard
    )

    await message.answer(text=_text('about1', 'ru'))
    await state.clear()

@router_main.message(StateFilter(FSM_state.wLang),F.text.endswith('nglish'))
@router_main.message(F.text.endswith('nglish'))
async def set_lang(message: types.Message, state: FSMContext):
    user_dict[message.from_user.id] = {'lang': 'en'}
    kb = [
        [
            types.KeyboardButton(text=_txt('solve', message.from_user.id)),
            types.KeyboardButton(text=_txt('reserch', message.from_user.id)),
            types.KeyboardButton(text=_txt('train', message.from_user.id))
        ],
        [
            types.KeyboardButton(text=_txt('speak', message.from_user.id)),
            types.KeyboardButton(text=_txt('AI', message.from_user.id)),
            types.KeyboardButton(text=_txt('Options', message.from_user.id)),

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(
        text=markdown.text(
            _txt('hello3', message.from_user.id),
            sep="\n"
        ),
        reply_markup=keyboard
    )

    await message.answer(text=_txt('about1', message.from_user.id))
    await state.clear()

# знакомый язык, но без словаря
@router_main.message(StateFilter(FSM_state.wLang), F.text.endswith('eutsche'))
@router_main.message(F.text.endswith('eutsche'))
async def set_lang(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('lang_known',message.from_user.id))
# незнакомый
@router_main.message(StateFilter(FSM_state.wLang))
async def set_lang(message: types.Message, state: FSMContext):
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