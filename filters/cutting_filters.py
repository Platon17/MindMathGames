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
        if message.text.lower().find(_txt('f_cut', message.from_user.id)) > 0:
            return True
        return False

class WordSolveCutting(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('sol', message.from_user.id)) == -1) and not (message.text.lower().find(_txt('cut', message.from_user.id)) == -1):
            return True
        return False

class RightCutting(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        np = message.text.count('+')
        if np > 3 and np <= 40:
            lines: list = message.text.split('\n')
            return {'matrix': lines,
                        'np': np
                          }
        return False

class BtnOption(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if (not (message.text.lower().find(_txt('f_n_cutting', message.from_user.id)) == -1) or
                not (message.text.lower().find(_txt('f_excess', message.from_user.id)) == -1) or
                not (message.text.lower().find(_txt('f_all_true', message.from_user.id)) == -1) or
                not (message.text.lower().find(_txt('f_all_false', message.from_user.id)) == -1)
        ):
            return True
        return False