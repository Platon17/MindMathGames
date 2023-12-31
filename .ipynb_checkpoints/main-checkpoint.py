import asyncio
import logging
from aiogram import Bot, Dispatcher,types
from aiogram.filters import CommandStart, Command
import config
from aiogram.enums import ParseMode
from aiogram.utils import markdown

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text= f"Hello, {message.from_user.full_name}")

@dp.message(Command("help"))
async def handle_start(message: types.Message):

    text = markdown.text(
        "Привет\\! Я умею играть в *игры*\\!",
        markdown.text(
            "Выбери в какую ",
            markdown.bold("игру"),
            "ты хочешь поиграть\\!",),
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
    )

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Something new 😐")


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())