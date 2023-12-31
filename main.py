import asyncio
import logging
from re import Match

from aiogram.types import ReplyKeyboardMarkup
from magic_filter import RegexpMode

from aiogram import Bot, F
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode

from config import settings

dp = Dispatcher()


@dp.message(Command("hello"))
async def hello(message: types.Message):
    url = "https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg"
    await message.answer(
        text=f"{markdown.hide_link(url)}Здравствуйте, {markdown.hbold(message.from_user.full_name)}. Чтобы начать играть нажмите кнопку '/start'. Чтобы обратиться за помощью нажмите кнопку '/help'.",
        parse_mode=ParseMode.HTML
    )


@dp.message(Command("start", "Назад"))
async def handle_start(message: types.Message):

    kb = [
        [
            types.KeyboardButton(text="Четно - нечетно"),
            types.KeyboardButton(text="Билетики"),
            types.KeyboardButton(text="Самый дорогой путь."),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите игру"
    )
    await message.answer(
        text=markdown.text(
            markdown.markdown_decoration.quote("Привет! Я умею играть в игры!"),
            markdown.text(
                "Выбери в ",
                markdown.bold("какую "),
                markdown.bold("игру"),
                markdown.markdown_decoration.quote("ты хочешь поиграть!"),
            ),
            sep="\n"
        ),
        reply_markup=keyboard
    )


@dp.message(F.text.lower() == "четно - нечетно")
async def chet(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Я буду решать, а ты загадывать"),
            types.KeyboardButton(text="Я буду задавать пример, а ты решать"),
            types.KeyboardButton(text="/Назад"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Кто из нас будет загадывать, а кто отвечать?",
    )
    await message.reply(
        text="Хороший выбор\\! Кто из нас будет загадывать, а кто отвечать\\?",
        reply_markup=keyboard
    )


@dp.message(F.text.lower() == "билетики")
async def biletik(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Я буду решать, а ты загадывать"),
            types.KeyboardButton(text="Я буду задавать пример, а ты решать"),
            types.KeyboardButton(text="/Назад"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Кто из нас будет загадывать, а кто отвечать?",
    )
    await message.reply(
        text="Хороший выбор\\! Кто из нас будет загадывать, а кто отвечать\\?",
        reply_markup=keyboard
    )


@dp.message(F.text.lower() == "самый дорогой путь.")
async def put(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Я буду решать, а ты загадывать"),
            types.KeyboardButton(text="Я буду задавать пример, а ты решать"),
            types.KeyboardButton(text="/Назад"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Кто из нас будет загадывать, а кто отвечать?",
    )
    await message.reply(
        text="Хороший выбор\\! Кто из нас будет загадывать, а кто отвечать\\?",
        reply_markup=keyboard
    )


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


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
