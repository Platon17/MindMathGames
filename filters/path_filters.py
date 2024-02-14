from aiogram.types import Message
from services.services import _txt, _some
from aiogram.filters import BaseFilter  # для создания своих фильтров
# >>> ================= BEST PATH ===========================
class WordPath(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('f_path',message.from_user.id)) == -1):
            return True
        return False

class WordSolvePath(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('f_solve',message.from_user.id)) == -1) and not (
                message.text.lower().find(_txt('f_path',message.from_user.id)) == -1):
            return True
        return False

class WordTrainPath(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not (message.text.lower().find(_txt('f_train', message.from_user.id)) == -1) and not (
                message.text.lower().find(_txt('f_path', message.from_user.id)) == -1):
            return True
        return False

class RightPath(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        lines: list = message.text.split('\n')
        m: list = [line.split() for line in lines]
        r = len(m)
        c = 0
        for row in m:
            cc = 0
            for s in row:
                if not s.isdigit():
                    return False
                cc += 1
                if c < cc: c = cc

        # дополняем исходную матрицу 0
        for i in range(r):
            for j in range(len(m[i]), c):
                m[i].append('0')

#        int_matrix = [[0] * c for i in range(r)]  # создаём пустую матрицу
#        for i in range(r):
#            for j in range(len(m[i]), c):
#                int_matrix = m[i][j]

        p: list[int][int] = [[0] * c for i in range(r)]  # mattrix
        for i in range(r):
            for j in range(c):
                p[i][j] = int(m[i][j])

        if p:
            return {'matrix': p}
        return False

class RightBestPath(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        best_path:int=int(message.text)
        if best_path>0:
            return {'best_path': best_path}
        return False

class WordGiveUp(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text.lower().find(_txt('f_give_up', message.from_user.id)) >= 0 :
            return True
        return False