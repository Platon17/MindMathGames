from aiogram.types import Message
from services.services import _txt, _some
from aiogram.filters import BaseFilter  # для создания своих фильтров
#from services.arturs import str_to_numbers
class WordArtur(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('f_artur', message.from_user.id)) != -1:
            return True
        return False


class WordSolveArtur(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if (message.text.lower().find(_txt('f_solve', message.from_user.id)) >= 0) and (message.text.lower().find(_txt('f_artur', message.from_user.id)) >= 0):
            return True
        return False

class WordTrainArtur(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if (message.text.lower().find(_txt('f_train', message.from_user.id)) >= 0) and (
                message.text.lower().find(_txt('f_artur', message.from_user.id)) >= 0):
            return True
        return False

class WordExamplArtur(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('f_exampl', message.from_user.id)) == -1) and not (
                message.text.lower().find(_txt('f_artur', message.from_user.id)) == -1):
            return True
        return False


class WordTainArtur(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('f_train', message.from_user.id)) == -1) and not (
                message.text.lower().find(_txt('f_artur', message.from_user.id)) == -1):
            return True
        return False

class WordGiveUp(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('f_give_up', message.from_user.id)) >= 0 :
            return True
        return False
# Ищет в сообщение то, что можно принять за билет (цифры)
class RightArtur(BaseFilter):
    async def __call__(self, message: Message)->bool:
        artur_dict: dict = {}
        artur_dict = str_to_numbers(message.text.replace(',', ' ').replace(':', ' ').replace(';', ' ').strip())
        if artur_dict:
            return artur_dict
        return False

class RightOpers(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.find('=')<0:
            return False
        opers = ""
        op = '+-*/_ ='
        for ch in message.text:
            if ch in op:
                if ch != ' ':
                    opers += ch
                else:
                    opers += '_'
        if opers: return {'opers': opers}
        return False