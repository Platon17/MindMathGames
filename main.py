import asyncio
import logging
from aiogram import Bot, Dispatcher,types
from aiogram.filters import CommandStart, Command
from config import settings
from aiogram.enums import ParseMode
from aiogram.utils import markdown


dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg"
    await message.answer(
        text= f"{markdown.hide_link(url)}Hello, {markdown.hbold(message.from_user.full_name)}",
        parse_mode=ParseMode.HTML
    )

@dp.message(Command("help"))
async def handle_start(message: types.Message):

    text = markdown.text(
        markdown.markdown_decoration.quote("Привет! Я умею играть в игры!"),
        markdown.text(
            "Выбери в ",
            markdown.underline("какую "),
            markdown.bold("игру"),
            markdown.markdown_decoration.quote("ты хочешь поиграть!"),
        ),
        sep = "\n"
    )
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)

@dp.message()
async def echo_message(message: types.Message):
    #await bot.send_message(
    #    chat_id=message.chat.id,
    #    text='Start Processing...',
    #)
    #await bot.send_message(
    #    chat_id=message.chat.id,
    #    text='Detected Message...',
    #    reply_to_message_id=message.message_id,
    #
    #)

    await message.answer(
        text='Wait...',
        parse_mode=None
    )

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Something new 😐")


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
        parse_mode = ParseMode.MARKDOWN_V2,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())