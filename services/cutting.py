import time                         # подключаем модуль time
from itertools import combinations  # составление комбинаций
from random import randint

def gen_cutting(min_r:int, max_r:int, min_c:int, max_c:int, procent:int)->list:
    r:int = randint(min_r,max_r)
    c:int = randint(min_c,max_c)
    m:list = [[False] * c for i in range(r)]  # пустая матрица
    for i in range(r*c*procent//100):
        p = randint(0,r*c-1)
        #m[p//c][p%c]=not m[p//c][p%c]
        m[p//c][p%c] = True
    return m

def gen_cutting_str(min_r:int, max_r:int, min_c:int, max_c:int, procent:int)->str:
    m:list = gen_cutting(min_r, max_r, min_c, max_c, procent)
    r = len(m)
    c = len(m[0])
    lines:list = []
    for y in range(r):
        line:str = ''
        for x in range(c):
            if m[y][x]:
                line=line+'+'
            else:
                line=line+'.'
        lines.append(line)
    return '\n'.join(lines)

# функция выдаёт уменьшенную матрицу без лишних строк и столбцов
# передаем функции набор точек
# функция возвращает матрицу
def fit(v:int,r:int,c:int)->list:
    x_max = 0
    x_min = c - 1
    y_max = 0
    y_min = r - 1
    for p in v:
        y = p//c
        x = p%c
        if y < y_min: y_min = y
        if y > y_max: y_max = y
        if x < x_min: x_min = x
        if x > x_max: x_max = x

    _c = x_max - x_min+1    # новое количество столбцов
    _r = y_max - y_min+1    # новое количество рядов
    nm = [[False] * _c for i in range(_r)]  # создаём пустую матрицу
    # переносим туда данные
    for p in v:
        y = p // c - y_min
        x = p % c - x_min
        nm[y][x] = True
    return nm

# функция выдаёт кортеж (список чисел) фигуры сдвинутой в угол
def cort(m:list,r:int,c:int)->tuple:
    _r:int=len(m)
    _c:int=0
    d: list = []
    for y in range(_r):
        _c =len(m[y])
        for x in range(_c):
            if m[y][x]:
                d.append(y*c+x)
    return tuple(d)

# поворачивает матрицу направо
def rotateL(g):
    return [[g[j][i] for j in range(len(g))] for i in range(len(g[0])-1,-1,-1)]
# поворачивает матрицу налево
def rotateR(g):
    return [[g[j][i] for j in range(len(g)-1,-1,-1)] for i in range(len(g[0]))]
# поворачивает матрицу на 180
def rotate(g):
    return [row[::-1] for row in g[::-1]]
# отражает матрицу по горизонтале
def rev_h(g):
    return [row[::-1] for row in g[::]]
# отражает матрицу по вертикали
def rev_v(g): # относительно диагонали
    return [row[::] for row in g[::-1]]

# передаем функции набор точек
# функция возвращает кортеж кортежей точек, которые равны
def variants(v:list[int],r:int,c:int) -> tuple:
    frames = []
    f = fit(v,r,c)                      # матрица обрезанная
    frames.append(cort(f,r,c))          # 1 оригинал
    f  = rotate(f)
    cf = cort(f,r,c)
    if not frames.count(cf):
        frames.append(cf)          # 180 поворот
    f = rotateL(f)
    cf = cort(f,r,c)
    if not frames.count(cf):
        frames.append(cf)         # +90 поворот налево
    f = rotate(f)
    cf = cort(f,r,c)
    if not frames.count(cf):
        frames.append(cf)          # -90 поворот 180
    f = rev_v(f)
    cf = cort(f,r,c)
    if not frames.count(cf):
        frames.append(cf)           # отражение
    f = rotate(f)
    cf = cort(f,r,c)
    if not frames.count(cf):
        frames.append(cf)          # 180 поворот
    f = rotateL(f)
    cf = cort(f,r,c)
    if not frames.count(cf):
        frames.append(cf)         # +90 поворот налево
    f = rotate(f)
    cf = cort(f,r,c)
    if not frames.count(cf):
        frames.append(cf)          # -90 поворот 180
    return tuple(frames)

def print_m(ttm:tuple, r:int, c:int, sch = 'XOTHSZAVBC', empty:str='_'):
    for y in range(r):
        for x in range(c):
            p = y * c + x           # номер координаты
            nt = 0                  # номер кортежа
            dot = False             # может точки нет ни в одном из кортежей
            for tm in ttm:          # кортеж внутри кортежа
                if tm.count(p):     # если координата есть в фигуре печатаем
                    print(sch[nt], end=' ')
                    dot = True      # точка есть в кортежах
                    continue        # следующую координату, в кортежах других фигур этой координаты не будет
                nt += 1             # следующий кортеж
            if not dot:             # если этой координаты нет ни в одном кортеже
                print(empty, end=' ')
        print()
    print()

def t_to_str(ttm:tuple, r:int, c:int, sch = 'XOTHSZAVBC', empty:str='_')->str:
    lines = ""
    for y in range(r):
        line = ""
        for x in range(c):
            p = y * c + x           # номер координаты
            nt = 0                  # номер кортежа
            dot = False             # может точки нет ни в одном из кортежей
            for tm in ttm:          # кортеж внутри кортежа
                if tm.count(p):     # если координата есть в фигуре печатаем
                    #print(sch[nt], end=' ')
                    line += sch[nt]
                    dot = True      # точка есть в кортежах
                    continue        # следующую координату, в кортежах других фигур этой координаты не будет
                nt += 1             # следующий кортеж
            if not dot:             # если этой координаты нет ни в одном кортеже
                #print('.', end=' ')
                line += empty
        lines+=line+'\n'
    return lines

def cutnn(ssm:list, sm:list, tdots:tuple, r:int, c:int, n:int, l:int, all:bool=False, nabor:tuple = ()):
    if not nabor:  # если набор ещё не задан
        first = True
    else:
        first = False

    if n == 1:   # базовое условие выхода из рекурсии
        lm = []
        for v in combinations(tdots, l):  	# перебираем варианты из tdots по l клеток
            tv = cort(fit(v,r,c),r,c)  			# преобразовываем вариант в кортеж
            if first:  # если набор ещё не задан, зададим его по первому варианту
                return v				
            if nabor.count(tv):         	# вариант существует в наборе
                sm.append(v)
                return v

    else:
        for v in combinations(tdots, l):      # перебираем варианты из tdots по l клеток
            # будем добавлять только уникальные решения
            unique = True
            for i_sm in ssm:
                if v in i_sm:
                    unique = False
                    break
            if not unique: continue

            tv = cort(fit(v,r,c),r,c)               # преобразовываем вариант в кортеж
            if first:
                nabor = variants(v,r,c)         # набор правильных кортежей
            if nabor.count(tv):             # если вариант есть в наборе, то этот вариант подходящий
                df = list(tdots)            # передаем кортеж в список
                for i in v: df.remove(i)    # убираем из списка координаты фигуры
                tv = cutnn(ssm,sm,tuple(df), r, c, n-1, l, all, nabor)
                if tv:
                    sm.append(v)
                    if not first:
                        return sm
                    else:
                        ssm.append(sm)
                        sm = []
                        if not all: return ssm # если нужен только один вариант выходим
        if first:
            return ssm


def cutn(tdots:tuple, r:int, c:int, n:int, excess:int=0, all:bool=False) -> tuple:
    l = (len(tdots) - excess) // n          # количество клеток в фигуре
    sm = []                     			# решение
    ssm = []                     			# решение
    ssm = cutnn(ssm,sm,tdots, r, c, n, l, all)  # запускаем рекурсию, возвращает список решений
    return tuple(ssm)

    # m
	# n
	# excess
	# all
	
def m_to_mb(m:str) -> dict:
    result:dict = {}
    mb:list=[]
    r: int = len(m)
    c: int = 0
    d: int = 0
    for s in m: 			# строка с клавиатуры
        str_mb:[bool] = []	# строка матрицы [True,False]
        cs = 0          	# количество символов в строке
        for ch in s:    	# перебираем символы в строке
            if ch.isdigit():        # если цифра
                k = int(ch)         # количество пустых клеток
                cs += k             # увеличим количество символов в строке на n
                for i in range(k):  # n пустых клеток
                    str_mb.append(False)
            else:
                cs += 1             # количество символов в строке на 1
                if ch == '+':       # если + то, это клетка фигуры
                    str_mb.append(True)
                    d += 1
                else:               # иначе пустая клетка
                    str_mb.append(False)
        if cs > c: c = cs           # максимально длинную строку храним в с
        mb.append(str_mb)  			# добавляем строку матрицы в исходную матрицу
    # дополняем исходную матрицу до квадратной матрицы
    if c < r:     # если количество колонок меньше количества строк, добавим строки пустыми символами 
        c = r
        for i in range(r):
            for j in range(len(mb[i]), c):
                mb[i].append(False)
    if r < c:           # если количество строк меньше количества колонок, добавим пустые строки
        for i in range(c - r):
            mb.append([False] * c)
        r = c
    result['mb']=mb
    result['r'] = r
    result['c'] = c
    result['d'] = d
    return result

def mb_to_dots(mb,r,c) -> list:		
    dots = []    # список с номерами клеток
    k = r * c   # количество клеток
    for i in range(k):
        if mb[i // c][i % c]:
            dots.append(i)
    return dots

def m_tostr(m, d:list[bool]=None, ch = '_XO')->str:
	line:str=''
	r:int=len(m)
	c:int=len(m[0])
	for y in range(0, r):
		for x in range(0, c):
			if m[y][x]:
				if d:
					if (y*c+x) in d:
						line = line + ch[2]
					else:
						line = line + ch[1]
				else:
					line = line + ch[1]
			else:
				line = line + ch[0]
		line = line + '\n'
	return line
def m_to_str(m:list)->dict:
    if not m: return ""
    mb_dict:dict=m_to_mb(m)
    mb = mb_dict['mb']
    r = mb_dict['r']
    c = mb_dict['c'] # количество колонок
    d = mb_dict['d'] # количество клеток в фигуре
    dots:list = mb_to_dots(mb,r,c)# список с номерами клеток
    sm:list=[]
    sm.append(dots)
    return t_to_str(tuple(sm), r, c)
def str_m(m_str:str)->list[bool]:
    dm: list[bool] = []   # матрицы
    c = 0  # количество колонок
    lines: list = m_str.split('\n')
    for line in lines:
        sm: list[bool] = []  # строка матрицы [True,False]
        cs = 0  # количество символов в строке
        for ch in line:  # перебираем символы в строке
            if (ch.isdigit()) and (ch != '0'):  # если цифра и не 0
                n = int(ch)  # количество пустых клеток
                cs += n  # увеличим количество символов в строке на n
                for j in range(n):  # n пустых клеток
                    sm.append(False)
            else:
                cs += 1  # количество символов в строке на 1
                if ch == '+':  # если + то, это клетка фигуры
                    sm.append(True)
                else:  # иначе пустая клетка
                    sm.append(False)
        if cs > c: c = cs  # максимально длинную строку храним в с
        dm.append(sm)  # добавляем строку матрицы в исходную матрицу
    return dm
def str_m_str(m_str:str)->str:
    return m_tostr(str_m(m_str))


def cut(m, n:int, excess:int=0, all:bool=False) -> dict:
    res_dict: dict[str,[int|bool|tuple]] = {}
#	lines:list[]=text.split('\n')
#	m:list=[line.split() for line in lines]
    if not m: return False
    mb_dict:dict=m_to_mb(m)
    mb = mb_dict['mb']
    r = mb_dict['r']
    c = mb_dict['c'] # количество колонок
    d = mb_dict['d'] # количество клеток в фигуре
    if (d - excess) % n != 0: return False
    # создадим кортеж в котором будут номера клеток фигуры
    dots:list = mb_to_dots(mb,r,c)# список с номерами клеток

    start = time.thread_time()
    ssm:tuple = cutn(tuple(dots),r,c,n, excess, all)
    result:list=[]
    for sm in ssm:
        result.append(t_to_str(sm, r, c))
    res_dict['result']=result
    res_dict['time']=time.thread_time() - start

    return res_dict

if __name__ == "__main__":
    print("Программ позволяет разрезать заданную фигуру на n одинаковых фигур")
    print("причем часть клеток могут остаться не использованными")
    r = int(input("Введите количество рядов в фигуре "))  # количество строк (рядов)
    dm = []     # исходная матрица
    c = 0       # количество колонок
    p = 0       # количество клеток в фигуре
    # ввод исходной матрицы с клавиатуры
    print("Фигура будет состоять из " + str(r) +" строк")
    print("введите поочередно все строки фигуры, где: ")
    print(" ""+"" - клетка фигуры;")
    print(" ""цифра"" - количество пустых клеток;")
    print(" ""любой другой символ"" - пустая клетка.")
    for i in range(r):
        s = input()     # строка с клавиатуры
        sm = []         # строка матрицы [True,False]
        cs = 0          # количество символов в строке
        for ch in s:    # перебираем символы в строке
            if ch.isdigit():        # если цифра
                n = int(ch)         # количество пустых клеток
                cs += n             # увеличим количество символов в строке на n
                for j in range(n):  # n пустых клеток
                    sm.append(False)
            else:
                cs += 1             # количество символов в строке на 1
                if ch == '+':       # если + то, это клетка фигуры
                    sm.append(True)
                    p += 1
                else:               # иначе пустая клетка
                    sm.append(False)
        if cs > c: c = cs           # максимально длинную строку храним в с
        dm.append(sm)  # добавляем строку матрицы в исходную матрицу

    # дополняем исходную матрицу до квадратной матрицы
    if c < r: c = r     # если количество колонок меньше количества строк, добавим строки пустыми символами
    for i in range(r):
        for j in range(len(dm[i]), c):
            dm[i].append(False)
    if r < c:           # если количество строк меньше количества колонок, добавим пустые строки
        for i in range(c - r):
            dm.append([False] * c)
        r = c

    t = int(input("Введите число на какое количество одинаковых частей нужно разбить фигуру:"))
    excess = int(input("Введите число ""лишних"" клеток фигуры, которое можно убрать:"))

    # фиксируем время старта работы кода
    start = time.thread_time()

    if (p - excess) % t != 0:
        print("Фигуру невозможно разбить!")
        exit()

    # создадим кортеж в котором будут номера клеток фигуры
    fdf = []    # список с номерами клеток
    k = r * c   # количество клеток
    for i in range(k):
        if dm[i // c][i % c]:
            fdf.append(i)
    tdots = tuple(fdf)    # преобразуем список в кортеж

    sm = []                     # список
    sm.append(fdf)              # добавляем туда кортеж
    print_m(tuple(sm),r,c)      # печатаем
    ssm = []                    # список решений
    ssm = cutn(tdots, t, False)
    for sm in ssm:
        print_m(tuple(sm), r, c)  # печатаем
    print(len(ssm))
    print("The end")
    finish = time.thread_time()  # фиксируем время окончания работы кода
    print('Время работы: ' + str(finish - start))  # вычитаем время старта из времени окончания и выводим результат

#empty = [[False] * c for i in range(r)]  # пустая матрица