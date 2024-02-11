# Хэндлеры главного меню
from var import user_dict
from data import FSM_state, max_variants
from filters.cutting_filters import WordCutting, WordSolveCutting, WordTrainCutting, WordTrainCutting, RightCutting
from filters.main_filters import strDict, WordExampl
from services.services import _txt, _sLine
from services.cutting import m_to_str,cut
from aiogram import Router
from aiogram.fsm.context import FSMContext


from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.utils import markdown
from aiogram.enums import ParseMode

# ==================================================
# >>> ================= CUTTING ====================
# ==================================================
router_cutting = Router()

@router_cutting.message(Command('cutting'))
@router_cutting.message(F.text.startwith('Разрезание'))
@router_cutting.message(F.text.startwith('разрезание'))
@router_cutting.message(F.text.startwith('Cutting'))
@router_cutting.message(F.text.startwith('cutting'))
@router_cutting.message(WordCutting())
async def cutting(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wCutting)
    await message.answer(text=_txt('chosen_cutting',message.from_user.id))
    await message.answer(text=_txt('need_cutting', message.from_user.id))
    kb = [
        [
            types.KeyboardButton(text=_txt('back', message.from_user.id)),
            types.KeyboardButton(text=_txt('home', message.from_user.id)),
            types.KeyboardButton(text=_txt('examples', message.from_user.id)),
            types.KeyboardButton(text=_txt('options', message.from_user.id)),
        ],
        [
            types.KeyboardButton(text='++++'),
            types.KeyboardButton(text='+..+\n+..+'),
            types.KeyboardButton(text='++++\n+..+\n+..+'),
            types.KeyboardButton(text='+..+\n+..+\n+..+\n+..+'),
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_txt('txt_solve_cutting', message.from_user.id)
    )
    await message.answer(
        text=markdown.text(
            _txt('txt_solve_cutting', message.from_user.id),
            markdown.text(_txt('input_citting', message.from_user.id),
                          ),
            sep="\n"
        ),
        reply_markup=keyboard
    )

# ==== EXAMPLES cutting ===
#@router_cutting.message(WordExamplCutting())
@router_cutting.message(StateFilter(FSM_state.wCutting), WordExampl())
#@router_cutting.message(StateFilter(FSM_state.wCutting), F.text == _txt('examples'))
async def examples_tickets(message: types.Message):
    await message.answer(text="keyboard with examples")
    kb = [
        [
            types.KeyboardButton(text=_txt('back', message.from_user.id)),
            types.KeyboardButton(text=_txt('home', message.from_user.id)),
            types.KeyboardButton(text='++++'),
        ],
        [

            types.KeyboardButton(text='+..+\n+..+'),
            types.KeyboardButton(text='++++\n+..+\n+..+'),
            types.KeyboardButton(text='+..+\n+..+\n+..+\n+..+'),
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_txt('txt_solve_tickets')
    )
    await message.answer(
        text=markdown.text(
            _txt('txt_solve_ticket'),
            markdown.text(_txt('input_ticket'),
                          ),
            sep="\n"
        ),
        reply_markup=keyboard
    )


@router_cutting.message(WordTrainCutting(), RightCutting())
@router_cutting.message(WordCutting(), RightCutting())
@router_cutting.message(StateFilter(FSM_state.wCutting), RightCutting())
async def solve_cutting(message: types.Message, state: FSMContext, matrix: list):

    await message.answer(text=_sLine(m_to_str(matrix)))

    userdata = await state.get_data()
    n_cutting = userdata.get('n_cutting', 4)
    excess_cutting = userdata.get('excess_cutting', 0)
    all_cutting = userdata.get('all_cutting', False)
    result = cut(matrix, n_cutting, excess_cutting, all_cutting)
    if result:
        res=result['result']
        for v in res:
            await message.answer(text=_sLine(v))
    else:
        await message.answer(text=_txt('not_solve_cutting', message.from_user.id))
    await message.answer(text=_txt('try_again_cutting', message.from_user.id))
    await state.set_state(FSM_state.wCutting)

# Options Cutting
@router_cutting.message(StateFilter(FSM_state.wCutting))
#    , F.text ==_txt('options', message.from_user.id))

async def to_options_cutting(message: types.Message):
    await message.answer(text=_txt('input_options', message.from_user.id))
    await message.answer(text='keyboard with options')
    await message.answer(text="keyboard with examples")
    kb = [
        [
            types.KeyboardButton(text='all_cutting=False'),
            types.KeyboardButton(text='n_cutting=3'),
            types.KeyboardButton(text='excess_cutting=1'),
        ],
        [
            types.KeyboardButton(text='all_cutting=True'),
            types.KeyboardButton(text='n_cutting=4'),
            types.KeyboardButton(text='excess_cutting=0'),
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_txt('print_options')
    )
    await message.answer(
        text=markdown.text(
            _txt('print_options'),
            markdown.text(_txt('print_options'),
                          ),
            sep="\n"
        ),
        reply_markup=keyboard
    )
    state.set_state(FSM_state.wCuttingOptions)

# answer Options Ticket
@router_cutting.message(StateFilter(FSM_state.wCuttingOptions))
#, F.text==_txt('options', message.from_user.id), strDict())

async def set_options_cutting(message: types.Message, state: FSMContext,key: str, value: str):
    if key == _txt('all_cutting', message.from_user.id):
        await state.update_data(all_cutting=bool(value))
        await message.answer(text=_txt('all_cutting', message.from_user.id) + '=' + value)
    elif key == _txt('n_cutting', message.from_user.id):
        await state.update_data(n_cutting=int(value))
        await message.answer(text=_txt('n_cutting', message.from_user.id) + '=' + value)
    elif key == _txt('excess_cutting', message.from_user.id):
        await state.update_data(excess_cutting=int(value))
        await message.answer(text=_txt('excess_cutting', message.from_user.id) + '=' + value)
    await message.answer(text=_txt('input_cutting', message.from_user.id))
    state.set_state(FSM_state.wCutting)

# ==== TRAIN CUTTING ===
@router_cutting.message(WordCutting())
#@router_cutting.message(TrainCutting())
#@router_cutting.message(StateFilter(FSM_state.wTrain), F.text == _txt('cutting'))
async def show_task_cutting(message: types.Message, state: FSMContext):
    # UNDER CONSTRUCTION
    await message.answer(text='lets_solve_cutting')
    await message.answer(text="print" + _txt('give_up', message.from_user.id) + " for give up")
    n = randint(3, 6)
    # matrix:list = []
    # for i in range(n)
    #	s = []
    #	line.append(choice('.+'))
    #	result = tickets.solve(numbers,all_tickets,'+-*/_')
    #	if result:
    #		await state.update_data(ticket=numbers)
    #		await state.update_data(ans_ticket=result)

    # await state.set_state(FSM_state.wAnsCutting)
    await message.answer(text=_txt('lets_do', message.from_user.id))
    await state.clear()

# GIVE UP
@router_cutting.message(StateFilter(FSM_state.wAnsCutting))
#, F.text==_txt('give_up', message.from_user.id))

async def give_up_Cutting(message: types.Message, state: FSMContext):
    # UNDER CONSTRUCTION
    #	userdata = await state.get_data()
    #	numbers = userdata.get['ticket']
    #	result = tickets.solve(numbers,True,'+-*/_')
    #	if result:
    #		for res in result:
    #			await message.answer(text=res)
    #	else:
    #		result  = userdata.get['result']
    #		for res in result:
    #			await message.answer(text=res)
    await message.answer(text=_txt('lets_do', message.from_user.id))
    await state.clear()

# TRY ANSWER
# UNDER CONSTRUCTION
# @router_cutting.message(StateFilter(FSM_state.wAnsCutting),RightOpers())
# async def ans_cutting(message: Message, opers:str):
# UNDER CONSTRUCTION
#	userdata = await state.get_data()
#	numbers = userdata.get['ticket']
#	if tickets.numbers_opers(numbers, opers):
#		await message.answer(text='you_are_right')
#		await message.answer(text='lets_solve_ticket')
# new ticket
#		is_find_ticket = False
#		while not is_find_ticket:
#			n = randint(5,10)
#			numbers:list = []
#			for i in range(n)
#				numbers.append(randint(5,10))
#			result = tickets.solve(numbers,False,'+-*/_')
#			if result:
#				await state.update_data(ticket=numbers)
#				await state.update_data(ans_ticket=result)
#	else
#		await message.answer(text=_txt('you_are_wrong',message.from_user.id))
#		await message.answer(text=_txt('lets_again_tickets',message.from_user.id))
#	await message.answer(text=_txt('lets_do',message.from_user.id))
#	await state.clear()

@router_cutting.message(WordCutting)
@router_cutting.message(StateFilter(FSM_state.wCutting))
async def wrong_cutting(message: types.Message):
    await message.answer(text='wrong_cutting')

    # ================= CUTTING =====================<<<


