from aiogram.types import Message
from services.services import _txt, _some
from aiogram.filters import BaseFilter  # для создания своих фильтров
#from services.simms import str_to_numbers
class WordSimm(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('f_simm', message.from_user.id)) != -1:
            return True
        return False


class WordSolveSimm(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if (message.text.lower().find(_txt('f_solve', message.from_user.id)) >= 0) and (message.text.lower().find(_txt('f_simm', message.from_user.id)) >= 0):
            return True
        return False

class WordTrainSimm(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if (message.text.lower().find(_txt('f_train', message.from_user.id)) >= 0) and (
                message.text.lower().find(_txt('f_simm', message.from_user.id)) >= 0):
            return True
        return False

class WordExamplSimm(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('f_exampl', message.from_user.id)) == -1) and not (
                message.text.lower().find(_txt('f_simm', message.from_user.id)) == -1):
            return True
        return False


class WordTainSimm(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('f_train', message.from_user.id)) == -1) and not (
                message.text.lower().find(_txt('f_simm', message.from_user.id)) == -1):
            return True
        return False

class WordGiveUp(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('f_give_up', message.from_user.id)) >= 0 :
            return True
        return False
# Ищет в сообщение то, что можно принять за билет (цифры)
class RightSimm(BaseFilter):
    async def __call__(self, message: Message)->bool:
        if message.text.count('+')>3:
            return True
        return False
