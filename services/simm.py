from copy import deepcopy
from random import randint

def gen_m(min_r:int, max_r:int, max_c:int, max_c:int, procent:int)->list:
	r:int = randint(min_n,max_n)
	c:int = randint(min_n,max_n)
	m:list = [[False] * c for i in range(r)]  # пустая матрица
	for i in range(r*c*procent//100)
		p = randint(0,r*c-1)
		m[p//c][p%c]=not m[p//c][p%c]
	return m

def m_to_str(m, d, ch = '_XO'):
    line:str=[]
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if m[y][x]:
		if d[y][x]:
		  line = line + ch[2]
		else:
	  	  line = line + ch[1]
            else:
                line = line + ch[0]
        line = line + '\n'
    returns line

def print_m(m,d, ch = '_XO'):
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if m[y][x]:
		if d[y][x]:
		  print(ch[2], end=' ')
		else:
	  	  print(ch[1], end=' ')
            else:
                print(ch[0], end=' ')
        print()
    print()

def dot(m,x,y,q=1):
    for i in range(0-q, 1+q):       # y
        for j in range(0-q, 1+q):   # x
            y_ = y + i
            x_ = x + j
            #print(x_,y_)
            if x_<c and y_<r and x_>=0 and y_>=0:
                m[y_][x_] = not(m[y_][x_])
    #print_m(m)

def solve(dm:list)->dict:
	result:dict={}	
	r:int=len(dm)
	if r=0: return result
	c:int=len(dm[0])
	k = r*c # количество клеток
	# поиск симметрий относительно точки
	best = k
	best_m = []
	best_d = []
	best_sd = 0
	for sy in range(1,2*(r-1)):
	    for sx in range(1,2*(c-1)):
	        d:list = []
	        for y in range(r):
	            for x in range(c):
	                if not dm[y][x]: continue   # если нет не будем искать симметрии
	                dy = 2*y - sy     # смещение точки симметрии от точки по y
	                dx = 2*x - sx     # смещение точки симметрии от точки по x
	                ry = (sy - dy) // 2     # x точка отражения относительно точки симметрии
	                rx = (sx - dx) // 2     # y точка отражения относительно точки симметрии
	                p = y * c + x
	                rp = ry * c + rx
	                if ry < 0 or ry >= r or rx < 0 or rx >= c: # если точка отражения выходит за границы
	                    d.append(p) # ошибочная точка
	                else:
	                    if not dm[ry][rx] : # если точка не совпадает с точкой симметрии
	                        d.append(p) # ошибочная точка
	        if len(d) <= best:
	            if len(d) < best:
	                best = len(d)
			best_m:list=[]
	            best_d = deepcopy(d)
		    best_m.append(best_d)
	            best_sd = sy//2 * c + sx//2
	
	# поиск симметрий горизонтальной линии
	for sy in range(0,2*(r-1)):
            d:list = []
	    for y in range(r):
	        for x in range(c):
	            if not dm[y][x]: continue  # если нет не будем искать симметрии
	            dy = 2*y - sy     # смещение точки симметрии от точки по y
	            dx = 0          # смещение точки симметрии от точки по x
	            ry = (sy - dy)//2    # x точка отражения относительно точки симметрии
	            rx = x          # y точка отражения относительно точки симметрии
	            p = y * c + x
	            rp = ry * c + rx
	            if ry < 0 or ry >= r or rx < 0 or rx >= c: # если точка отражения выходит за границы
	                d.append(p) # ошибочная точка
	            else:
	                if not dm[ry][rx]: # если точка не совпадает с точкой симметрии
	                    d.append(p) # ошибочная точка
	    if len(d) <= best:
	        if len(d) < best:
	            best = len(d)
		    best_m:list=[]
	        best_d = deepcopy(d)
		best_m.append(best_d)
	        best_sd = sy//2 * c
	
	# поиск симметрий относительно вертикальной линии
	for sx in range(0, 2*(c - 1)):
	    d = []
	    for y in range(r):
	        for x in range(c):
	            if not dm[y][x]: continue  # если нет не будем искать симметрии
	            dy = 0  # смещение точки симметрии от точки по y
	            dx = 2 * x - sx  # смещение точки симметрии от точки по x
	            ry = y  # x точка отражения относительно точки симметрии
	            rx = (sx - dx) //2  # y точка отражения относительно точки симметрии
	            p = y * c + x
	            rp = ry * c + rx
	            if ry < 0 or ry >= r or rx < 0 or rx >= c:  # если точка отражения выходит за границы
	                d.append(p)  # ошибочная точка
	            else:
	                if not dm[ry][rx]:  # если точка не совпадает с точкой симметрии
	                    d.append(p)  # ошибочная точка
	    if len(d) <= best:
	        if len(d) < best:
	            best = len(d)
		    best_m:list=[]
	        best_d = deepcopy(d)
		best_m.append(best_d)
	        best_sd = sx//2
	
	# поиск симметрий диагональ сверху вниз
	for s in range(-r+1,r-1):
	    d = []
	    for y in range(r):
	        for x in range(c):
	            if not dm[y][x]: continue  # если нет не будем искать симметрии
	            ry = x - s     # x точка отражения относительно точки симметрии
	            rx = y + s     # y точка отражения относительно точки симметрии
	            p = y * c + x
	            rp = ry * c + rx
	            if ry < 0 or ry >= r or rx < 0 or rx >= c: # если точка отражения выходит за границы
	                d.append(p) # ошибочная точка
	            else:
	                if not dm[ry][rx]: # если точка не совпадает с точкой симметрии
	                    d.append(p) # ошибочная точка
	    if len(d) <= best:
	        if len(d) < best:
	            best = len(d)
		    best_m:list=[]
	        best_d = deepcopy(d)
		best_m.append(best_d)
	        best_sd = 0
	
	# поиск симметрий диагональ снизу вверх
	for s in range(0,1):
	    d = []
	    for y in range(r):
	        for x in range(c):
	            if not dm[y][x]: continue  # если нет не будем искать симметрии
	            ry = c-1-x + s     # x точка отражения относительно точки симметрии
	            rx = c-1-y + s     # y точка отражения относительно точки симметрии
	            p = y * c + x
	            rp = ry * c + rx
	            if ry < 0 or ry >= r or rx < 0 or rx >= c: # если точка отражения выходит за границы
	                d.append(p) # ошибочная точка
	            else:
	                if not dm[ry][rx]: # если точка не совпадает с точкой симметрии
	                    d.append(p) # ошибочная точка
	    if len(d) <= best:
	        if len(d) < best:
	            best = len(d)
		    best_m:list=[]
	        best_d = deepcopy(d)
		best_m.append(best_d)
	        best_sd = k
	return {'result':best_m}
	
def unuse:
	print(best,best_d)
	# печатем ответ
	m = deepcopy(empty)
	dot(m, best_sd % c, (best_sd // c) % r, 0)
	print_m(m,'0')
	
	m = deepcopy(empty)
	for i in best_d:
	    dot(m, i % c, (i // c) % r, 0)
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
    if r < c:           # если количество строк меньше количества колонок, добавим пустые строки
        for i in range(c - r):
            dm.append([False] * c)
        r = c
    # фиксируем время старта работы кода
    start = time.thread_time()

    fdf = []    # список с номерами клеток
    k = r * c   # количество клеток
    for i in range(k):
        if dm[i // c][i % c]:
            fdf.append(i)
    tdots = tuple(fdf)    # преобразуем список в кортеж

    sm = []                     # список
    sm.append(fdf)              # добавляем туда кортеж
    print_m(tuple(sm),r,c)      # печатаем

    results:dict = solve(dm).['result']
    for res in results:
        print(m_to_str(dm,res))  # печатаем
    print("The end")
    finish = time.thread_time()  # фиксируем время окончания работы кода
    print('Время работы: ' + str(finish - start))  # вычитаем время старта из времени окончания и выводим результат