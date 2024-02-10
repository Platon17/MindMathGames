# Хэндлеры главного меню
from var import user_dict
from data import FSM_state, max_variants
from filters.tickets_filters import WordTicket, WordSolveTicket, WordGiveUp, WordExamplTicket, WordTrainTicket, RightTicket, RightOpers
from filters.main_filters import strDict, WordExampl, WordOptions
from services.services import _txt


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