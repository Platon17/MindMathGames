from aiogram.types import Message
from services.services import _txt
from aiogram.filters import BaseFilter  # для создания своих фильтров

class strDict(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        s = message.text.strip().lower()
        pEq = s.find('=')
        if pEq == -1:
            key = s[:pEq - 1]
            value = s[pEq + 1]
            return {'key': key, 'value': value}
        return False


class WordExampl(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('exampl', message.from_user.id)) != -1:
            return True
        return False


class WordOptions(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('options', message.from_user.id)) != -1:
            return True
        return False