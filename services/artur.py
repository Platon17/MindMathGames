n,g = map(int,input().split())
m = n*g
r = []
p = []
for i in range(n):
    r.append(0)
    p.append(0)
r[n//2]=m
do = True
st = 0
print(str(st)+">",*r)
while do:
    d = 0
    for i in range(n):
        s = r[i] // 2
        p[i-1] = p[i-1] + s
        if i + 1 < n:
            p[i+1] = p[i+1] + s
        else:
            p[0] = p[0] + s
        r[i] = r[i] - 2*s
    for i in range(n):
        r[i] = r[i] + p[i]
        p[i] = 0
        if (r[i] == g):
            d += 1
        if (r[i] == 0) or (r[i] == g*2):
            d += 1
    st=st+1
    print(str(st)+">",*r)
    if d == n:
        do = False