# Хэндлеры главного меню
from aiogram import Router
from aiogram.fsm.state import default_state, State, StatesGroup
from handlers import tickets_handlers

class FSM_state(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    mm = State()
    sm = State()
    wStrTickets = State()
    wResult = State()
    wAll = State()

# Инициализируем роутер уровня модуля
router_tasks = Router()
router_tasks.include_router(tickets_handlers.router_tickets)  # роутеры Билетики
#router_tasks.include_router(solve_handlers.router_cutting)  # роутеры Разрезание
#router_tasks.include_router(solve_handlers.router_bestPath) # роутеры Лучший путь
#router_tasks.include_router(solve_handlers.router_simm)     # роутеры Симметрия