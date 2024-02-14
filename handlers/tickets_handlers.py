# Хэндлеры главного меню
from var import user_dict
from data import FSM_state, max_variants
from filters.tickets_filters import WordTicket, WordSolveTicket, WordGiveUp, WordExamplTicket, WordTrainTicket, RightTicket, RightOpers
from filters.main_filters import strDict, WordExampl, WordOptions
from services.services import _txt,_sLine
from services.tickets import numbers_opers,gen_ticket, solve as ticket_solve

from aiogram import Router
from aiogram.fsm.context import FSMContext


from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.utils import markdown
from keyboards.keyboards import create_inline_kb, create_kb, create_kb_ru
from aiogram.enums import ParseMode
from handlers import tickets_handlers

# Инициализируем роутер уровня модуля
router_tickets = Router()


@router_tickets.message(StateFilter(FSM_state.wAnsTicket),F.text=='🔧 Настройки')
@router_tickets.message(StateFilter(FSM_state.wAnsTicket),F.text.endswith('астройки'))
@router_tickets.message(StateFilter(FSM_state.wAnsTicket),F.text.endswith('ptions'))
@router_tickets.message(StateFilter(FSM_state.wTicket),F.text=='🔧 Настройки')
@router_tickets.message(StateFilter(FSM_state.wTicket),F.text.endswith('астройки'))
@router_tickets.message(StateFilter(FSM_state.wTicket),F.text.endswith('ptions'))
async def to_options_tickets(message: types.Message, state: FSMContext):
    userdata = await state.get_data()
    operates = userdata.get('operates', '+-*/_')
    all_tickets = userdata.get('all_tickets', True)
    await message.answer(
        text=_txt('tickets_оptions',message.from_user.id),
        reply_markup=create_kb(2,message.from_user.id, 'btn_back', 'btn_home', 'btn_all_'+str(all_tickets), 'btn_opers_'+operates)
    )
    await state.set_state(FSM_state.wTicketOptions)


# ==== TRAIN TICKET ===
@router_tickets.message(WordTrainTicket())
@router_tickets.message(StateFilter(FSM_state.wTrain),WordTicket())
async def show_task_ticket(message: types.Message, state: FSMContext):
    await message.answer(text='solve_ticket')
    userdata = await state.get_data()
    operates = userdata.get('operates', '+-*/_')
    all_tickets = userdata.get('all_tickets', True)
    numbers=gen_ticket(4, 8, 9, operates)
    await state.update_data(ticket=numbers)
    await message.answer(
        text=_sLine('    '.join(numbers)),
        reply_markup=create_kb(2,message.from_user.id, 'btn_back', 'btn_home', 'btn_options', 'btn_give_up')
    )

    await message.answer(text='for_give_up')
    await state.set_state(FSM_state.wAnsTicket)

# GIVE UP
@router_tickets.message(StateFilter(FSM_state.wAnsTicket), F.text=='🤲 Сдаюсь!')
@router_tickets.message(StateFilter(FSM_state.wAnsTicket), WordGiveUp())
async def give_up_ticket(message: types.Message,state: FSMContext):
    userdata = await state.get_data()
    numbers = userdata.get('ticket')
    operates = userdata.get('operates', '+-*/_')
    all_tickets = userdata.get('all_tickets', True)
    result = ticket_solve(numbers, 0, all_tickets, operates)
    if result:
        await message.answer(text=_txt('result_ticket1', message.from_user.id))
        n_variants = len(result['result'])
        if n_variants > max_variants:
            await message.answer(text=_txt('result_only_max', message.from_user.id))
        elif len(result['result'])>1:
            await message.answer(text=_txt('result_all1', message.from_user.id))
        # выводить не боллее max_variants ответов
        n_var=1
        for res in result['result']:
            if n_var > max_variants:
                break
            await message.answer(text=_sLine(res))
            n_var += 1
    else:
        await message.answer(text=_txt('wrong1', message.from_user.id)+'gu')

    await state.set_state(FSM_state.wAnsTicket)
    await show_task_ticket(message,state)
# TRY ANSWER
@router_tickets.message(StateFilter(FSM_state.wAnsTicket), RightOpers())
async def ans_ticket(message: types.Message, opers: str, state: FSMContext):
    userdata = await state.get_data()
    numbers = userdata.get('ticket')
    operates = userdata.get('operates', '+-*/_')
    all_tickets = userdata.get('all_tickets', True)
    if numbers_opers(numbers, opers):
        await message.answer(text=_txt('right', message.from_user.id))
        await message.answer(text=_txt('solve_ticket', message.from_user.id))
        numbers = gen_ticket(6, 6, 9, operates)
        await message.answer(text='  '.join(numbers))
        await state.update_data(ticket=numbers)
        await message.answer(text=_txt('for_give_up', message.from_user.id))
    else:
        await message.answer(text=_txt('try_again',message.from_user.id))
@router_tickets.message(StateFilter(FSM_state.wAnsTicket))
async def ans_ticket2(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('wrong_ticket', message.from_user.id))
@router_tickets.message(StateFilter(FSM_state.wAnsTicket))
async def wrong_ans_ticket(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('try_again_ticket', message.from_user.id))


@router_tickets.message(Command('tickets'))
@router_tickets.message(F.text.startwith('Билет'))
@router_tickets.message(F.text.startwith('билет'))
@router_tickets.message(F.text.startwith('Ticekt'))
@router_tickets.message(F.text.startwith('ticekt'))
@router_tickets.message(WordTicket())
async def tickets(message: types.Message, state: FSMContext):
    await message.answer(
        text=markdown.text(_txt('need_tickets',message.from_user.id),sep="\n"),
        reply_markup=create_kb(4,message.from_user.id, 'btn_back', 'btn_home', 'btn_examples', 'btn_options',
                               '    '.join(gen_ticket(4, 6, 9, '+-*/')),
                               '    '.join(gen_ticket(5, 7, 9, '+-*/')),
                               '    '.join(gen_ticket(6, 8, 9, '+-*/')),
                               '    '.join(gen_ticket(7, 9, 12, '+-*/')),
                               '    '.join(gen_ticket(8, 10, 15, '+-*/')))
    )
    await state.set_state(FSM_state.wTicket)


# ==== EXAMPLES TICKETS ===
@router_tickets.message(WordExamplTicket())
@router_tickets.message(StateFilter(FSM_state.wTicket), WordExampl())
async def examples_tickets(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=_txt('back', message.from_user.id)),
            types.KeyboardButton(text=_txt('home', message.from_user.id)),
            types.KeyboardButton(text='1231234=9'),
        ],
        [
            types.KeyboardButton(text='1 2 3 4 5 6'),
            types.KeyboardButton(text='2 2 2 2 = 8'),
            types.KeyboardButton(text='1 2 3 4 7 8'),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(
        text='',
        reply_markup=keyboard
    )

# ==== SOLVE TICKET ===
#получение и решение Билетика
@router_tickets.message(WordTicket(), RightTicket())
@router_tickets.message(StateFilter(FSM_state.wTicket), RightTicket())
async def solve_ticket(message: types.Message, state: FSMContext, numbers: list, pos_eq:int):
    userdata = await state.get_data()
    operates = userdata.get('operates', '+-*/_')
    all_tickets = userdata.get('all_tickets', True)
    result = ticket_solve(numbers, pos_eq, all_tickets, operates)
    if result:
        await message.answer(text=_txt('result_ticket1', message.from_user.id))
        n_variants = len(result['result'])
        if n_variants > max_variants:
            await message.answer(text=_txt('result_only_max', message.from_user.id))
        elif len(result['result'])>1:
            await message.answer(text=_txt('result_all1', message.from_user.id))
        n_var=1
        for res in result['result']:
            if n_var > max_variants:
                break
            await message.answer(text=_sLine(res))
            n_var += 1
    else:
        await message.answer(text=_txt('wrong1', message.from_user.id)+"solve ticket")
    await message.answer(text=_txt('wait_more1', message.from_user.id))
    await state.set_state(FSM_state.wTicket)


# Options Ticket


@router_tickets.message(StateFilter(FSM_state.wTicketOptions),F.text=='⬅️ Назад')
async def options_back(message: types.Message, state: FSMContext):

    await state.set_state(FSM_state.wTicket)
    await show_task_ticket(message,state)

@router_tickets.message(StateFilter(FSM_state.wTicketOptions))
async def set_options_tickets_dall(message: types.Message, state: FSMContext):
    if message.text == _txt('btn_all_True',message.from_user.id):
        await state.update_data(all_tickets=False)
    elif message.text == _txt('btn_all_False',message.from_user.id):
        await state.update_data(all_tickets=True)
    elif message.text == _txt('btn_opers_+-*/_', message.from_user.id):
        await state.update_data(operates='+-')
    elif message.text == _txt('btn_opers_+-', message.from_user.id):
        await state.update_data(operates='+-*/')
    elif message.text == _txt('btn_opers_+-*/', message.from_user.id):
        await state.update_data(operates='+-*/_')
    await to_options_tickets(message,state)


# @router_tickets.message(WordTicket)
@router_tickets.message(StateFilter(FSM_state.wTicket))
async def wrong_ticket(message: types.Message, state: FSMContext,):
    #await message.answer(text=_txt('wrong_ticket', message.from_user.id))
    await message.answer(text=_txt('wrong_ticket', message.from_user.id))
    await message.answer(text=_txt('need_tickets', message.from_user.id))
