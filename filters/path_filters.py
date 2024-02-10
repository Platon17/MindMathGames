# >>> ================= BEST PATH ===========================
    class WordPath(BaseFilter):
        async def __call__(self, message: Message) -> bool:
            if not (message.text.lower().find(_txt('path')) == -1):
                return True
            return False

    class WordSolvePath(BaseFilter):
        async def __call__(self, message: Message) -> bool:
            if not (message.text.lower().find(_txt('sol')) == -1) and not (
                    message.text.lower().find(_txt('path')) == -1):
                return True
            return False

    class WordTainPath(BaseFilter):
        async def __call__(self, message: Message) -> bool:
            if not (message.text.lower().find(_txt('train', message.from_user.id)) == -1) and not (
                    message.text.lower().find(_txt('path', message.from_user.id)) == -1):
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

            int_matrix = [[0] * c for i in range(r)]  # создаём пустую матрицу
            for i in range(r):
                for j in range(len(m[i]), c):
                    int_matrix = m[i][j]

            if int_matrix:
                return {'matrix': matrix,
            'n_row': r,
            'n_col': c}
            return False
