from aiogram.types import Message, Game
from aiogram import Bot, F
from aiogram import Dispatcher





# ==== EXAMPLES PATH ===
#@dp.message(WordExamplPath())
@dp.message(StateFilter(FSM_state.wPath), WordExampl())
@dp.message(StateFilter(FSM_state.wPath), F.text == _text('examples'))
async def examples_tickets(message: Message):
    await message.answer(text="keyboard with examples")
    kb = [
        [
            types.KeyboardButton(text=_text('back')),
            types.KeyboardButton(text=_text('home')),
            types.KeyboardButton(text='1 2 3 4 5 6 7'),
        ],
        [
            types.KeyboardButton(text='1 2 3 4 5 6'),
            types.KeyboardButton(text='7 6 8 9 6 8'),
            types.KeyboardButton(text='9 4 3 2 3 5'),
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_text('txt_solve_path')
    )
    await message.answer(
        text=markdown.text(
            _text('txt_solve_path'),
            markdown.text(_text('input_path'),
                          ),
            sep="\n"
        ),
        reply_markup=keyboard
    )

#@dp.message(WordPath(), RightPath())
@dp.message(StateFilter(FSM_state.wPath))
async def solve_path(message: Message, state: FSMContext, matrix: list, n_raw: int, n_col: int):
    result = find_path(matrix, n_raw, n_col)
    if result:
        await message.answer(text=result.get['rout'])
        await message.answer(text=result.get['path'])
    else:
        await message.answer(text=_text('not_solve_path', lang))
    await message.answer(text=_text('try_again_path', lang))
    state.set_state(FSM_state.wPath)

#@dp.message(WordPath())
@dp.message(StateFilter(FSM_state.wPath))
async def wrong_path(message: Message):
    await message.answer(text='wrong_path')

    # ================= BEST PATH =====================<<<
    # =====================================================

    # HOME
    # ГЛАВНОЕ МЕНЮ
    # срабатывает всегда если сброшено состояние
    # @router_mm.message(StateFilter(default_state))
    @dp.message(StateFilter(default_state))
    @dp.message(F.text == _text('home', lang))
    async def toMainMenu(message: types.Message, state: FSMContext):
        await message.answer(text=_text('lets_do', lang))
        await state.clear()

    kb = [
        [
            types.KeyboardButton(text=_text('solve', lang)),
            types.KeyboardButton(text=_text('reserch', lang)),
            types.KeyboardButton(text=_text('train', lang))
        ],
        [
            types.KeyboardButton(text=_text('speak', lang)),
            types.KeyboardButton(text=_text('AI', lang)),
            types.KeyboardButton(text=_text('Options', lang)),

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_text('choice_actions', lang)
    )
    await message.answer(
        text=markdown.text(
            _text('mm', lang),
            markdown.text(_text('choice_actions', lang),
                          ),
            sep="\n"
        ),
        reply_markup=keyboard
    )

# BACK
@dp.message(F.text==_text('back', lang))

async def to_back(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_do', lang))
    await state.clear()

# SOLVE
@dp.message(F.text == _text('solve', lang))
async def solve(message: types.Message, state: FSMContext):
    kb = [
        [
            types.KeyboardButton(text=_text('tickets')),
            types.KeyboardButton(text=_text('cutting')),
            types.KeyboardButton(text=_text('best_path')),
            types.KeyboardButton(text=_text('simm'))
        ],
        [types.KeyboardButton(text=_text('back')),
         types.KeyboardButton(text=_text('home')),
         types.KeyboardButton(text=_text('lang')),
         types.KeyboardButton(text=_text('cancel')),
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
    await state.set_state(FSM_state.wSolve)

# RESERCH
@dp.message(F.text == _text('reserch', lang))
async def to_reserch(message: Message):
    await message.answer(text=_text('lets_do', lang))
    state.set_state(FSM_state.wReserch)

# TRAIN
@dp.message(F.text==_text('train', lang))

async def to_train(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_do', lang))

    kb = [
        [
            types.KeyboardButton(text=_text('tickets')),
            types.KeyboardButton(text=_text('cutting')),
            types.KeyboardButton(text=_text('best_path')),
            types.KeyboardButton(text=_text('simm'))
        ],
        [types.KeyboardButton(text=_text('back')),
         types.KeyboardButton(text=_text('home')),
         types.KeyboardButton(text=_text('lang')),
         types.KeyboardButton(text=_text('cancel')),
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
    await state.set_state(FSM_state.wTrain)

# Options
@dp.message(F.text==_text('options', lang))

async def to_options(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_do', lang))
    state.set_state(FSM_state.wOptions)

# ===== LAST CATCHERS =====
@dp.message(StateFilter(FSM_state.wSolve))
async def past_wSolve(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wSolve', lang))

    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wReserch))
async def past_wReserch(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wReserch', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wTrain))
async def past_wTrain(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wTrain', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wAI))
async def past_wAI(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wAI', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wOptions))
async def past_wOptions(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wOptions', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wLang))
async def past_wLang(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wLang', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wTicket))
async def past_wTicket(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wTicket', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wAnsTicket))
async def past_wAnsTicket(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wAnsTicket', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wCutting))
async def past_wCutting(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wCutting', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wAnsCutting))
async def past_wAnsCutting(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wAnsCutting', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wPath))
async def past_wPath(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wPath', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(FSM_state.wAnsPath))
async def past_wAnsPath(message: Message, state: FSMContext):
    await message.answer(text=_text('lets_clear_state', lang) + _text('wAnsPath', lang))
    await state.clear()
    await message.answer(text=_text('lets_do', lang))

@dp.message(StateFilter(default_state))
async def past_default_state(message: Message, state: FSMContext):
    await message.answer(text=_text('nobody_catch_me', lang))
    await message.answer(text=_text('lets_do', lang))

@dp.message()
async def past_all(message: Message, state: FSMContext):
    await message.answer(text=_text('nobody_catch_me', lang))
    await message.answer(text=_text('lets_do', lang))
    await state.clear()

    kb = [
        [
            types.KeyboardButton(text=_text('solve', lang)),
            types.KeyboardButton(text=_text('reserch', lang)),
            types.KeyboardButton(text=_text('train', lang))
        ],
        [
            types.KeyboardButton(text=_text('speak', lang)),
            types.KeyboardButton(text=_text('AI', lang)),
            types.KeyboardButton(text=_text('Options', lang)),

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_text('choice_actions', lang)
    )
    await message.answer(
        text=markdown.text(
            _text('mm', lang),
            markdown.text(_text('choice_actions', lang),
                          ),
            sep="\n"
        ),
        reply_markup=keyboard
    )