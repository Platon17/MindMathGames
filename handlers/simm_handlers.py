# Хэндлеры главного меню
from var import user_dict
from data import FSM_state, max_variants
from filters.simm_filters import WordSimm, WordTainSimm, WordSolveSimm, WordExamplSimm, WordTrainSimm, WordGiveUp, RightSimm
from keyboards.keyboards import create_inline_kb, create_kb, create_kb_ru
#WordSimm, WordSolveTicket, WordGiveUp, WordExamplTicket, WordTrainTicket, RightTicket, RightOpers
from filters.main_filters import strDict, WordExampl, WordOptions
from services.services import _txt,_sLine
from services.simm import solve_simm_str, gen_simm_str, str_m_str, m_to_str, str_to_m

from aiogram import Router
from aiogram.fsm.context import FSMContext

from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from handlers import tickets_handlers

# Инициализируем роутер уровня модуля
router_simm = Router()


@router_simm.message(StateFilter(FSM_state.wSimm), F.text=='🎲 Случайный пример')
async def examples_tickets(message: types.Message, state: FSMContext):
    await simm(message,state)
# ==== TRAIN SIMM ===
@router_simm.message(WordTrainSimm())
@router_simm.message(StateFilter(FSM_state.wPath),WordSimm())
async def show_task_Simm(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('solve_simm', message.from_user.id))
    simm=gen_simm_str(5,10,5,10,20)
    await state.update_data(simm=simm)
    await message.answer(
        text= simm,
        reply_markup=create_kb(2,message.from_user.id, 'btn_back', 'btn_home','btn_give_up')
    )
    await message.answer(text=_txt('for_give_up', message.from_user.id))
    await state.set_state(FSM_state.wAnsSimm)

# GIVE UP
@router_simm.message(StateFilter(FSM_state.wAnsSimm), F.text=='🤲 Сдаюсь!')
@router_simm.message(StateFilter(FSM_state.wAnsSimm), WordGiveUp())
async def give_up_simm(message: types.Message,state: FSMContext):
    userdata = await state.get_data()
    simm = userdata.get('simm')
    results = solve_simm_str(simm)
    if results:
        result=results.get('result')
        for res in results:
            await message.answer(text=_sLine(res))
        else:
            await message.answer(text=_txt('not_solve_simm',message.from_user.id))
#    await state.set_state(FSM_state.wAnsSimm)
    await show_task_simm(message,state)



# TRY ANSWER
@router_simm.message(StateFilter(FSM_state.wAnsTicket), RightSimm())
async def ans_Simm(message: types.Message, best_simm: int, state: FSMContext):
    userdata = await state.get_data()
    simm = userdata.get('simm')
    results = solve_simm_str(simm)
    if results:
        result=results.get('result')
        if message.text in results:
           await message.answer(text=_txt('right', message.from_user.id))
        else:
            await message.answer(text=_txt('try_again',message.from_user.id))
    else:
        await message.answer(text=_txt('not_solve_simm',message.from_user.id))

@router_simm.message(StateFilter(FSM_state.wAnsSimm))
async def ans_simm_wrong(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('wrong_simm', message.from_user.id))


#@router_simm.message(message.text == _txt('Simm'))
@router_simm.message(F.text.startwith('simm'))
@router_simm.message(Command('simm'))
#@router_simm.message(F.text.startwith('Билет'))
#@router_simm.message(F.text.startwith('билет'))
@router_simm.message(F.text.startwith('Simm'))
@router_simm.message(F.text.startwith('simm'))
@router_simm.message(WordSimm())
async def simm(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wSimm)
    # examples buttons
    BTN_EXMPL:dict={}
    for i in range(6):
        BTN_EXMPL['btn_exmpl_' + str(i)] = gen_simm_str(8, 12, 8, 12, 15)
    await message.answer(text=_txt('quote100', message.from_user.id))
    await message.answer(
        text=markdown.text(
            _txt('txt_solve_simm', message.from_user.id),
            markdown.text(_txt('input_simm', message.from_user.id),
                          ),
            sep="\n"
        ),
        reply_markup=create_kb(3,message.from_user.id, 'btn_back', 'btn_home', 'btn_examples', **BTN_EXMPL)

    )

@router_simm.message(StateFilter(FSM_state.wSimm), RightSimm())
#@router_simm.message(WordSimm())
async def solve_simm(message: types.Message, state: FSMContext):
    await message.answer(text=_sLine(str_m_str(message.text)))
    results = solve_simm_str(message.text)
    if results:
        results=results.get('result')
        for res in results:
            await message.answer(text=_sLine(m_to_str(str_to_m(message.text),res)))
    else:
        await message.answer(text=_txt('not_solve_simm',message.from_user.id))
    await message.answer(text=_txt('try_again_simm',message.from_user.id))
    await state.set_state(FSM_state.wSimm)

@router_simm.message(StateFilter(FSM_state.wSimm))
async def wrong_simm(message: types.Message):
    await message.answer(text='wrong_simm')
