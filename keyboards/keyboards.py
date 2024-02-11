from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup
from services.services import _txt,_text,_sLine
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder,KeyboardBuilder

# Функция для формирования инлайн-клавиатуры на лету
def create_inline_kb(width: int,
                     id: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=_txt(button,id),
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=_txt(text,id),
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()

def create_kb(width: int,
                     id: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = ReplyKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[KeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(KeyboardButton(
                text=_txt(button,id),
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(KeyboardButton(
                text=_txt(text,id),
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup(resize_keyboard=True)

def create_kb_ru(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = ReplyKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[KeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(KeyboardButton(
                text=_text(button,'ru'),
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(KeyboardButton(
                text=_text(text,'ru'),
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup(resize_keyboard=True)
