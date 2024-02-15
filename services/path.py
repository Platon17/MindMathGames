from random import randint
#import numpy as np

def str_to_list(text:str)->str:
    lines: list = text.split('\n')
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

    p: list[int][int] = [[0] * c for i in range(r)]  # mattrix
    for i in range(r):
        for j in range(c):
            p[i][j] = int(m[i][j])
    return p


def gen_path(min_n:int, max_n:int, min_m:int, max_m:int, min_p:int, max_p:int)->list:
    n = randint(min_n,max_n)
    m = randint(min_m, max_m)
    p:list[int][int] = [[0] * m for i in range(n)] # mattrix
    for y in range(n):
        for x in range(m):
            p[y][x]=randint(min_p,max_p)
    return p

def gen_path_str(min_n:int, max_n:int, min_m:int, max_m:int, min_p:int, max_p:int)->str:
    p = gen_path(min_n, max_n, min_m, max_m, min_p, max_p)
    n = len(p)
    m = len(p[0])
    lines:list = []
    for y in range(n):
        line:str = ''
        for x in range(m):
            line=line+str(p[y][x])+' '
        lines.append(line)
    return '\n'.join(lines)

def find_path(p:list)->dict:
    n = len(p)
    m = len(p[0])
    res_dict: dict[str,[list|int|bool|tuple]] = {}
    a:list[int][int] = [[0] * m for i in range(n)] # mattrix

    a[0][0] = p[0][0]
    for j in range(1, m):
        a[0][j] = a[0][j - 1] + p[0][j]
    for i in range(1, n):
        a[i][0] = a[i - 1][0] + p[i][0]
    for i in range(1, n):
        for j in range(1, m):
            a[i][j] = max(a[i][j - 1], a[i - 1][j]) + p[i][j]
    r_max = a[-1][-1]
 #   path:list[tuple]=[]
    s = []
    i = n - 1
    j = m - 1
#    path.append(tuple[i,j])
    while i != 0 or j != 0:
 #       path.append(tuple[i,j])
        if i == 0:
            s.append("R")
            j -= 1
        elif j == 0:
            s.append("D")
            i -= 1
        elif a[i][j - 1] > a[i - 1][j]:
            s.append("R")
            j -= 1
        else:
            s.append("D")
            i -= 1
#    path.append(tuple[0,0])
    rout = s[::-1]
    res_dict['best']=str(r_max)
    res_dict['rout']=''.join(rout)
#    res_dict['path']=path

    return res_dict
	
if __name__ == "__main__":
    print("")
    print("")
#    n = input("input raws: ")
#    m = input("input columns: ")
    print("Input mattrix")
    p = gen_path(5,10,5,10,1,9)
    print(gen_path_str(5,10,5,10,1,9))
    n = len(p)
    m = len(p[0])
    res_dict = find_path(p)
    print(res_dict['path'])
    print(res_dict['rout'])