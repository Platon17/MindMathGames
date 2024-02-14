# Хэндлеры главного меню
from keyboards.keyboards import create_inline_kb, create_kb, create_kb_ru
from var import user_dict
from data import FSM_state, max_variants
from filters.path_filters import WordPath, WordSolvePath,  RightPath, WordGiveUp, WordTrainPath, RightBestPath
from services.services import _txt, _sLine, _sPath

from aiogram import Router
from aiogram.fsm.context import FSMContext
from services.path import gen_path, gen_path_str, find_path

from aiogram import F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.utils import markdown
from aiogram.enums import ParseMode

# Инициализируем роутер уровня модуля
router_path = Router()

# ==== TRAIN PATH ===
@router_path.message(WordTrainPath())
@router_path.message(StateFilter(FSM_state.wPath),WordPath())
async def show_task_path(message: types.Message, state: FSMContext):
    await message.answer(text='solve_path')
    path = gen_path_str(8,8,8,8,6,9)
    await state.update_data(path=path)
    await message.answer(
        text=path,
        reply_markup=create_kb(2,message.from_user.id, 'btn_back', 'btn_home','btn_give_up')
    )
    await message.answer(text='for_give_up')
    await state.set_state(FSM_state.wAnsPath)

# GIVE UP
@router_path.message(StateFilter(FSM_state.wAnsPath), F.text=='🤲 Сдаюсь!')
@router_path.message(StateFilter(FSM_state.wAnsPath), WordGiveUp())
async def give_up_ticket(message: types.Message,state: FSMContext):
    userdata = await state.get_data()
    path = userdata.get('path')
    result = find_path(path, len(path),len(path[0]))
    if result:
        best:int=result.get('best')
        rout:str=result.get('rout')
        path:list=result.get('path')
        await message.answer(text=_sLine(str(best)))
        await message.answer(text=_sPath(rout))
        await message.answer(text=str(*path))
    else:
        await message.answer(text=_txt('not_solve_path',message.from_user.id))
#    await state.set_state(FSM_state.wAnsPath)
    await show_task_path(message,state)



# TRY ANSWER
@router_path.message(StateFilter(FSM_state.wAnsTicket), RightBestPath())
async def ans_path(message: types.Message, best_path: int, state: FSMContext):
    userdata = await state.get_data()
    path = userdata.get('path')
    result = find_path(path, len(path),len(path[0]))
    if result:
        best:int=result.get('best')
        rout:str=result.get('rout')
        path:list=result.get('path')
        if best==best_path:
            await message.answer(text=_txt('right', message.from_user.id))
            await message.answer(text=_sPath(rout))
            await message.answer(text=_sLine(str(best)))
            await message.answer(text=str(*path))
        else:
            await message.answer(text=_txt('try_again',message.from_user.id))
    else:
        await message.answer(text=_txt('not_solve_path',message.from_user.id))

@router_path.message(StateFilter(FSM_state.wAnsPath))
async def ans_wrong(message: types.Message, state: FSMContext):
    await message.answer(text=_txt('wrong_path', message.from_user.id))


#@router_path.message(message.text == _txt('path'))
@router_path.message(F.text.startwith('path'))
@router_path.message(Command('path'))
#@router_path.message(F.text.startwith('Билет'))
#@router_path.message(F.text.startwith('билет'))
@router_path.message(F.text.startwith('Path'))
@router_path.message(F.text.startwith('path'))
@router_path.message(WordPath())
async def path(message: types.Message, state: FSMContext):
    await state.set_state(FSM_state.wPath)
    # examples buttons
    BTN_EXMPL:dict={}
    for i in range(4):
        BTN_EXMPL['btn_exmpl_'+str(i)]=gen_path_str(7,7,7,7,6,9)
    await message.answer(
        text=markdown.text(
            _txt('txt_solve_path',message.from_user.id),
            markdown.text(_txt('input_path', message.from_user.id),
                          ),
            sep="\n"
        ),
        reply_markup=create_kb(4,message.from_user.id, 'btn_back', 'btn_home', 'btn_examples', 'btn_options',**BTN_EXMPL)

    )

@router_path.message(StateFilter(FSM_state.wPath), RightPath())
#@router_path.message(WordPath())
async def solve_path(message: types.Message, state: FSMContext, matrix: list):
    result = find_path(matrix)
    if result:
        await message.answer(text=_sPath(result.get('rout')))
        await message.answer(text=_sLine(result.get('best')))
#        await message.answer(text=result.get('path'))
    else:
        await message.answer(text=_txt('not_solve_path',message.from_user.id))
    await message.answer(text=_txt('try_again_path', message.from_user.id))
    state.set_state(FSM_state.wPath)

@router_path.message(StateFilter(FSM_state.wPath))
async def wrong_path(message: types.Message):
    await message.answer(text='wrong_path')

@router_path.message()
async def wrong_path(message: types.Message):
    await message.answer(text='wrong_path')
