from random import randint
import numpy as np

def gen_path(min_n:int, max_n:int, min_m:int, max_m:int, min_p:int, max_p:)->list:
	return = np.random.randint(min_p,max_p,(randint(min_m,max_m),randint(min_n,max_n)))

def find_path(p:list, n:int, m:int)->dict:
    res_dict: dict[str,[list|int|bool|tupl]] = {}
    	
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
    path:list[tulip]=[]
    s = []
    i = n - 1
    j = m - 1
    path.append(tulip(i,j))
    while i != 0 or j != 0:
        path.append(tulip(i,j))
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
    rout = str(*s[::-1])
    res_dict['best']=r_max
    res_dict['rout']=rout
    res_dict['path']=path

    return res_dict
	
if __name__ == "__main__":
    print("")
    print("")
    n = input("input raws: ")
    m = input("input columns: ")
    print("Input mattrix")
    p = [list(map(int, input().split())) for i in range(n)]
    # ��������� ����� ������ ������ ����
    start = time.thread_time()
    res_dict = find_path(p, n, m)
    print(res_dict['path'])
    print(res_dict['rout'])
    finish = time.thread_time()  # ��������� ����� ��������� ������ ����
    print('����� ������: ' + str(finish - start))  # �������� ����� ������ �� ������� ��������� � ������� ���������