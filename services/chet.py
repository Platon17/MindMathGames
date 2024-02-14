import time                         # подключаем модуль time
from copy import deepcopy
from random import randint
from itertools import combinations  # составление комбинаций

def gen_chet(min_r:int, max_r:int, min_c:int, max_c:int, procent:int)->list:
	r:int = randint(min_r,max_r)
	c:int = randint(min_c,max_c)
	m:list = [[False] * c for i in range(r)]  # пустая матрица
	for i in range(r*c*procent//100):
		p = randint(0,r*c-1)
		m[p//c][p%c]=not m[p//c][p%c]
	return m

def gen_chet_str(min_r:int, max_r:int, min_c:int, max_c:int, procent:int)->str:
	m:list = gen_chet(min_r, max_r, min_c, max_c, procent)
	r = len(m)
	c = len(m[0])
	lines:list = []
	for y in range(r):
		line:str = ''
		for x in range(c):
			if m[y][x]:
				line=line+'+'
			else:
				line=line+'_'
		lines.append(line)
	return '\n'.join(lines)


def m_to_str(m:list[bool],ch='_X')->str:
    line:str = ''
    for y in range(0, len(m)):
        for x in range(0, len(m[0])):
            if m[y][x]:
                line = line + ch[1]
            else:
                line = line + ch[0]
        line = line + '\n'
    return line
	
	
def print_m(m:list[bool],ch='_X'):
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if m[y][x]:
                print(ch[1], end=' ')
            else:
                print(ch[0], end=' ')
        print()
    print()

def dot(m:list[bool],x,y,q=1)->list:
    r:int = len(m)
    c:int = len(m[0])
    for i in range(0-q, 1+q):       # y
        for j in range(0-q, 1+q):   # x
            y_ = y + i
            x_ = x + j
            if x_<c and y_<r and x_>=0 and y_>=0:
                m[y_][x_] = not(m[y_][x_])
    return m

def dot_to_str(dots, r:int,c:int,ch:str='_X')->str:
    m = [[False] * c for i in range(r)]    # пустая матрица
    for dot in dots:
        m[dot//r][dot%c] = True
    return m_to_str(m,ch)

def solve(mb:list,q:int=1,all:bool=False)->dict:
    result:dict={}
    r:int=len(mb)
    if r==0: return result
    c:int=len(mb[0])
    empty = [[False] * c for i in range(r)]    # пустая матрица
    k = r*c 		# количество клеток
    results:list=[]
    v_dots: list = []  # матрица точек
    for i in range(k):
        v_dots.append(i)
    for kd in range(1,k+1):
        for dots in combinations(v_dots,kd):
            m:list = deepcopy(empty)
            for p in dots:
                m = dot(m,p%c,(p//c)%k,q)
            if m == mb:
                results.append(dots)
                if not all:
                    break
    lines:list=[]
    for dots in results:
        lines.append(dot_to_str(dots,r,c))
    result['result'] = lines
    return result


def str_to_m(m_str:str)->list[bool]:
    dm: list[bool] = []   # матрицы
    c:int = 0  # количество колонок
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
                if ch == '+':
                    sm.append(True)
                else:
                    sm.append(False)
                if cs > c:
                    c = cs
        dm.append(sm)
    for i in range(len(dm)):
        for j in range(len(dm[i]), c):
            dm[i].append(False)
    return dm

def str_m_str(m_str:str)->str:
	return m_to_str(str_to_m(m_str))


def solve_chet_str(m_str:str,q:int=1,all:bool=False)->dict:
    result:dict={}
    res = solve(str_to_m(m_str), q, all)
    result['result'] = res.get('result')
    return result
	
	
def unuse():
			
	# печатем ответ
	m = deepcopy(empty)
	for i in d:
		dot(m, i%c, (i//c)%r, 0)
	print_m(m)

if __name__ == "__main__":
    r = int(input("Введите количество рядов в фигуре "))  # количество строк (рядов)
    dm = []     # исходная матрица
    c = 0       # количество колонок
    p = 0       # количество клеток в фигуре
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
    ldots = solve(dm,False).get('result')
    for dots in ldots:
        print(dot_to_str(dots,r,c))