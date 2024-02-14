from aiogram.fsm.state import default_state, State, StatesGroup
class FSM_state(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    wSolve = State()
    wReserch = State()
    wTrain = State()
    wAI = State()
    wSpeak = State()

    wOptions = State()
    wLang = State()
    wTicket = State()
    wTicketOptions = State()
    wAnsTicket = State()
    wCutting = State()
    wCuttingOptions = State()
    wAnsCutting = State()
    wPath = State()
    wAnsPath = State()
    wSimm = State()
    wAnsSimm = State()
    wChet = State()
    wAnsChet = State()
    wArtur = State()
    wArturCoin = State()

idPlaton = 1157076572
max_variants = 30
max_n_tickets = 15