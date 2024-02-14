# Хэндлеры главного меню
from var import user_dict
from data import FSM_state, max_variants
from filters.artur_filters import WordArtur
    #WordTicket, WordSolveTicket, WordGiveUp, WordExamplTicket, WordTrainTicket, RightTicket, RightOpers)
from filters.main_filters import strDict, WordExampl, WordOptions
from services.services import _txt
from services.artur import solve

from aiogram import Router
from aiogram.fsm.context import FSMContext


from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from handlers import tickets_handlers

# Инициализируем роутер уровня модуля
router_artur = Router()

#@router_path.message(message.text == _txt('artur'))
@router_artur.message(F.text.startwith('artur'))
@router_artur.message(Command('artur'))
#@router_artur.message(F.text.startwith('Билет'))
#@router_artur.message(F.text.startwith('билет'))
@router_artur.message(F.text.startwith('Artur'))
@router_artur.message(F.text.startwith('artur'))
@router_artur.message(WordArtur())
@router_artur.message(StateFilter(FSM_state.wReserch))
async def artur(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wArtur)
    await message.answer(
        text=markdown.text(
            _txt('txt_solve_artur'),
            markdown.text(_txt('input_artur_k', message.from_user.id),
                          ),
            sep="\n"
        ),
        reply_markup=create_kb(4,message.from_user.id, 'btn_back', 'btn_home')
    )

@router_artur.message(StateFilter(FSM_state.wArtur),
lambda x: x.text.isdigit() and 1 <=int(x.text)<=100)
async def artur_coin(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wArturCoin)
    await state.update_data(knights=int(message.text))
    await message.answer(
        text=markdown.text(
            _txt('txt_solve_artur_c'),
            markdown.text(_txt('input_artur_c', message.from_user.id),
                          ),
            sep="\n"
        ),
        reply_markup=create_kb(4,message.from_user.id, 'btn_back', 'btn_home')
    )

@router_artur.message(StateFilter(FSM_state.wArtur))
async def wrong_knights(message: types.Message):
    await message.answer(text='wrong_knights')

@router_artur.message(StateFilter(FSM_state.wArturCoin),
lambda x: x.text.isdigit() and 1 <=int(x.text)<=1000)
async def artur_research(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wArtur)
    await state.update_data(coins=int(message.text))
    userdata = await state.get_data()
    knights = userdata.get('knights')
    coins = userdata.get('coins')
    result = solve(knights,coins)
    if result:
        sucsess:int=result.get('sucsess')
        status:str=result.get('status')
        n_op:list=result.get('n_op')

#	if len(result)<n_artur_op:
    if len(result)<30:
        for r in status:
            await message.answer(text=' '.join(r))
        else:
            for i in range(10):
                await message.answer(text=' '.join(status[i]))
            await message.answer(text='...')
            for i in range(n_op-10,n_op):
                await message.answer(text=' '.join(status[i]))

    await message.answer(text=_txt('artur_n_op', message.from_user.id)+n_op)
    await message.answer(text=_txt('artur_sucsess', message.from_user.id)+sucsess)
    await artur(message, state)

@router_artur.message(StateFilter(FSM_state.wArturCoin))
async def wrong_knights(message: types.Message):
    await message.answer(text='wrong_coins')
