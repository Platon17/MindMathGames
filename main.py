import asyncio
import logging
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, Game
from aiogram import Bot, F
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from bilet import bilet
import config
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from FindPath import find_path
from handlers import mm_handlers, solve_handlers
from services.services import _text

# === FSM ===
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

idPlaton = 1157076572
async def start_bot(bot: Bot):
    await bot.send_message(idPlaton, text="Бот запущен!")
async def stop_bot(bot: Bot):
    await bot.send_message(idPlaton, text="Бот остановлен!")

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(Command("help", prefix="/"))
async def handle_start(message: types.Message):
    text = markdown.text(
        markdown.markdown_decoration.quote("Привет! Я умею играть в игры\\!"),
        markdown.text(
            "Для начала игры нажми кнопку ",
            markdown.bold('/start'),
            markdown.markdown_decoration.quote("\\. Далее нажимай на кнопки и следуй указаниям\\."),
        ),
        sep="\n"
    )
    kb = [
        [
            types.KeyboardButton(text="/start")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=keyboard)



# команда СТАРТ
# состояние отсутствует
@dp.message(Command('start'), StateFilter(default_state))
async def handle_start(message: types.Message, state: FSMContext):
    kb = [
        [
            types.KeyboardButton(text=_text('langRU')),
            types.KeyboardButton(text=_text('langEN')),
            types.KeyboardButton(text=_text('langOther'))
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=_text('choice_lang')
    )
    await message.answer(
        text=markdown.text(
            _text('Hello1'),
            markdown.text(_text('choice_lang'),
            ),
            sep="\n"
        ),
        reply_markup=keyboard
    )

## Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
@dp.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text='Вы вышли из машины состояний\n\n'
             'Чтобы снова перейти к заполнению анкеты - '
             'отправьте команду /fillform'
    )
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()

@dp.message(Command("hello"))
async def hello(message: types.Message):
    url = "https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg"
    await message.answer(
        text=_text('Hello2'),
        parse_mode=ParseMode.HTML
    )


# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
# создаём класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSM_state(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    choise_lang = State()   # Состояние ожидания выбора языка
    fill_name = State()     # Состояние ожидания ввода имени
    choise_action = State() # Состояние ожидания выбора действия
    choise_task = State()   # Состояние ожидания выбора задачи

# Создаем "базу данных" пользователей
user_dict: dict[int, dict[str, str | int | bool]] = {}

async def main():
    #
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=config.BOT_TOKEN,
        parse_mode=ParseMode.HTML,
    )
    #dp.startup.register(start_bot)     # отправить сообщение о включении бота
    #dp.shutdown.register(stop_bot)     # отправить сообщение о выключение бота

    #dp.message.register(handle_start)

    # Регистриуем роутеры в диспетчере
    dp.include_router(mm_handlers.router)   # роутеры главного меню
    dp.include_router(solve_handlers.router)  # роутеры решать
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())