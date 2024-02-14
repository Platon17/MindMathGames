from aiogram.types import Message
from services.services import _txt, _some
from aiogram.filters import BaseFilter  # для создания своих фильтров
# >>> ================= Chet ===========================
class WordChet(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('f_chet', message.from_user.id)) != -1:
            return True
        return False

class WordSolveChet(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('f_solve', message.from_user.id)) == -1) and not (
                message.text.lower().find(_txt('f_chet', message.from_user.id)) == -1):
            return True
        return False

class WordTainChet(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('f_train', message.from_user.id)) == -1) and not (
                message.text.lower().find(_txt('f_chet', message.from_user.id)) == -1):
            return True
        return False

# если в тексет больше 3 плюсов +-
class RightChet(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.count('+')>3: return True
        return True
            