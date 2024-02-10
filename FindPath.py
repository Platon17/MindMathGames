def find_path(n, m):
    p = [list(map(int, input().split())) for i in range(n)]
    a = [[0] * m for i in range(n)]
    a[0][0] = p[0][0]
    for j in range(1, m):
        a[0][j] = a[0][j - 1] + p[0][j]
    for i in range(1, n):
        a[i][0] = a[i - 1][0] + p[i][0]
    for i in range(1, n):
        for j in range(1, m):
            a[i][j] = max(a[i][j - 1], a[i - 1][j]) + p[i][j]
    print(a[-1][-1])
    s = []
    i = n - 1
    j = m - 1
    while i != 0 or j != 0:
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

    return str(*s[::-1])
