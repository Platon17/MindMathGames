def solve(k:int,m:int)->dict:
    result: dict = {}
    if m % k != 0: return result
    g:int = m // k   # монет на человека
    r:list[int] = []
    p:list[int] = []
    for i in range(k):
        r.append(0)
        p.append(0)
    r[k // 2] = m
    do = True
    status:list=[]
    cut: list = []
    success: bool = False
    status.append(tuple(r))
    while do:
        d = 0
        nd = 0
        for i in range(k):
            s = r[i] // 2
            r[i] = r[i] - 2 * s
            p[i - 1] = p[i - 1] + s
            if i + 1 < k:
                p[i + 1] = p[i + 1] + s
            else:
                p[0] = p[0] + s
        for i in range(k):
            r[i] = r[i] + p[i]
            p[i] = 0
            if (r[i] == g):
                d += 1
            if (r[i] == 0) or (r[i] == g * 2):
                nd += 1
        status.append(tuple(r))
        if (d == k) or (nd == k):
            do = False
    if d == k:
        success = True

    if success:
        result['n_op']=len(status)
    else:
        result['n_op']=0
    result['status']=status
    result['sucsess']=success

    return result

if __name__ == "__main__":
    print("")
    print("")
    k, c = map(int, input("input knights and coins").split())
    result = solve(k, c)
    print(result.get('sucsess'))
    print(result.get('n_op'))
    for r in result.get('status'):
        print(str(*r))