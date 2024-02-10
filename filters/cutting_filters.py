from aiogram.types import Message
from services.services import _txt, _some
from aiogram.filters import BaseFilter  # для создания своих фильтров

class WordExamplCutting(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('exampl', message.from_user.id)) == -1) and not (message.text.lower().find(_txt('cutt', message.from_user.id)) == -1):
            return True
        return False

class WordTrainCutting(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('train', message.from_user.id)) == -1) and not (message.text.lower().find(_txt('cutt', message.from_user.id)) == -1):
            return True
        return False

class WordCutting(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('f_cut', message.from_user.id)) != -1:
            return True
        return False

class WordTicket(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('f_ticket', message.from_user.id)) != -1:
            return True
        return False


class WordSolveCutting(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('sol', message.from_user.id)) == -1) and not (message.text.lower().find(_txt('cut', message.from_user.id)) == -1):
            return True
        return False

class RightCutting(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        lines: list = message.text.split('\n')
        matrix: list = [line.split() for line in lines]
        if matrix: return {'matrix': matrix}
        return False
