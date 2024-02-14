# Хэндлеры главного меню
from var import user_dict
from data import FSM_state, max_variants
from filters.chet_filters import WordChet, WordTainChet, WordSolveChet, RightChet
    #WordTicket, WordSolveTicket, WordGiveUp, WordExamplTicket, WordTrainTicket, RightTicket, RightOpers)
from filters.main_filters import WordGiveUp, WordExampl, WordOptions
from services.services import _txt, _sLine
from services.chet import solve_chet_str, gen_chet_str, m_to_str, str_m_str
from keyboards.keyboards import create_inline_kb, create_kb, create_kb_ru


from aiogram import Router
from aiogram.fsm.context import FSMContext


from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from handlers import tickets_handlers

# Инициализируем роутер уровня модуля
router_chet = Router()



# ==== TRAIN chet ===
#@router_chet.message(WordTrainChet())
@router_chet.message(StateFilter(FSM_state.wTrain),WordChet())
async def show_task_chet(message: types.Message, state: FSMContext):
    await message.answer(text='solve_chet')
    chet=gen_chet_str(3,6,3,6,50)
    await state.update_data(chet=chet)
    await message.answer(
        text= _sLine(m_to_str(chet)),
        reply_markup=create_kb(2,message.from_user.id, 'btn_back', 'btn_home','btn_give_up')
    )
    await message.answer(text='for_give_up')
    await state.set_state(FSM_state.wAnsChet)

# GIVE UP
@router_chet.message(StateFilter(FSM_state.wAnsChet), F.text=='рџ¤І РЎРґР°СЋСЃСЊ!')
@router_chet.message(StateFilter(FSM_state.wAnsChet), WordGiveUp())
async def give_up_chet(message: types.Message,state: FSMContext):
    userdata = await state.get_data()
    chet = userdata.get('chet')
    results = solve_chet(chet)
    if results:
        for line in results:
            await message.answer(text=_sLine(line))
    else:
        await message.answer(text=_txt('not_solve_chet',message.from_user.id))
    await show_task_chet(message,state)

# TRY ANSWER
@router_chet.message(StateFilter(FSM_state.wAnsChet), RightChet())
async def ans_chet(message: types.Message, chet: list, state: FSMContext):
    userdata = await state.get_data()
    chet = userdata.get('chet')
    results = solve_chet_str(chet)
    if results:
        if message.text in results.get('result'):
            await message.answer(text=_txt('right', message.from_user.id))
        else:
            await message.answer(text=_txt('try_again',message.from_user.id))
    else:
        await message.answer(text=_txt('not_solve_chet',message.from_user.id))

@router_chet.message(StateFilter(FSM_state.wAnsChet))
async def ans_chet_wrong(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('wrong_chet', message.from_user.id))


#@router_chet.message(message.text == _txt('chet'))

@router_chet.message(Command('chet'))
@router_chet.message(F.text.startwith('Чётн'))
@router_chet.message(F.text.startwith('Четн'))
@router_chet.message(F.text.startwith('чётн'))
@router_chet.message(F.text.startwith('четн'))
@router_chet.message(F.text.startwith('Chet'))
@router_chet.message(F.text.startwith('chet'))
@router_chet.message(WordChet())
async def chet(message: types.Message, state: FSMContext):
    # examples buttons
    BTN_EXMPL:dict={}
    for i in range(4):
        BTN_EXMPL['btn_exmpl_'+str(i)]=gen_chet_str(5,10,5,10,20)

    await message.answer(
        text=markdown.text(
            _txt('txt_solve_chet', message.from_user.id),
            markdown.text(_txt('input_chet', message.from_user.id),
                          ),
            sep="\n"
        ),
        reply_markup=create_kb(4,message.from_user.id, 'btn_back', 'btn_home', 'btn_examples', 'btn_options',**BTN_EXMPL)

    )
    await state.set_state(FSM_state.wChet)


@router_chet.message(StateFilter(FSM_state.wChet), RightChet())
async def solve_chet(message: types.Message, state: FSMContext):
    await message.answer(text=_sLine(str_m_str(message.text)))
    results = solve_chet_str(message.text)
    if results:
        result=results.get('result')
        for line in result:
            await message.answer(text=_sLine(line))
    else:
        await message.answer(text=_txt('not_solve_chet',message.from_user.id))
    await message.answer(text=_txt('try_again_chet',message.from_user.id))
    state.set_state(FSM_state.wChet)

@router_chet.message(StateFilter(FSM_state.wChet))
async def wrong_chet(message: types.Message):
    await message.answer(text='wrong_chet')
