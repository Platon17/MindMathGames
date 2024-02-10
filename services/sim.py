from copy import deepcopy
def print_m(m, ch = 'X'):
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if m[y][x]:
                print(ch, end=' ')
            else:
                print('.', end=' ')
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

r = int(input())            # количество строк (рядов)
dm =[]                      # исходная матрица
c = 0                       # количество колонок
for i in range(r):
    s = input()             # строка
    sm=[]                   # строку превращаем в список
    cs = 0                  # количество символов в строке
    for ch in s:
        if ch.isdigit():
            n = int(ch)
            cs += n
            for j in range(n):
                sm.append(False)
        else:
            cs += 1             # количество символов в строке
            if ch == '+':       # если + то там поставим Х
                sm.append(True)
            else:               # иначе считаем клетки пустые
                sm.append(False)
    if cs > c:
        c = cs
    dm.append(sm)           # добавляем строку в матрицу
# дополняем матрицу fm до прямоугольной матрицы
for i in range(r):
    for j in range(len(dm[i]), c):
        dm[i].append(False)
print_m(dm)

empty = [[False] * c for i in range(r)]    # пустая матрица

k = r*c # количество клеток

# поиск симметрий относительно точки
best = k
best_d = []
best_sd = 0
for sy in range(1,2*(r-1)):
    for sx in range(1,2*(c-1)):
        d = []
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
        if len(d) < best:
            best = len(d)
            best_d = deepcopy(d)
            best_sd = sy//2 * c + sx//2

# поиск симметрий горизонтальной линии
for sy in range(0,2*(r-1)):
    d = []
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
    if len(d) < best:
        best = len(d)
        best_d = deepcopy(d)
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
    if len(d) < best:
        best = len(d)
        best_d = deepcopy(d)
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
    if len(d) < best:
        best = len(d)
        best_d = deepcopy(d)
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
    if len(d) < best:
        best = len(d)
        best_d = deepcopy(d)
        best_sd = k

print(best,best_d)
# печатем ответ
m = deepcopy(empty)
dot(m, best_sd % c, (best_sd // c) % r, 0)
print_m(m,'0')

m = deepcopy(empty)
for i in best_d:
    dot(m, i % c, (i // c) % r, 0)
print_m(m)