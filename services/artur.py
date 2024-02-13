def solve(k:int,m:int)->dict:
   result:dict={}
   if m%k!= 0: return result
   g = m%k
   r = []
   p = []
   for i in range(k):
    r.append(0)
    p.append(0)
   r[n//2]=m
   do = True
   status = 0
   cut:list=[]
   sucsecc:bool=False
#   print(str(st)+">",*r)
   while do:
    status.append(r)
    d = 0
    nd = 0
    for i in range(k):
        s = r[i] // 2
	r[i] = r[i] - 2*s        
	p[i-1] = p[i-1] + s
        if i + 1 < k:
            p[i+1] = p[i+1] + s
        else:
            p[0] = p[0] + s
    for i in range(k):
        r[i] = r[i] + p[i]
        p[i] = 0
        if (r[i] == g):
            d += 1
        if (r[i] == 0) or (r[i] == g*2):
            nd += 1
    st=st+1
#    print(str(st)+">",*r)
    if (d == k) or (d == k):
        do = False
   if d == k:
    sucsess= True:
   result['status':status]
   result['sucsess':sucsess]
   result['n_op':st]
   return:result

if __name__ == "__main__":
    print("")
    print("")
    k,c = map(int,input("input knights and coins").split())
    solve(k,c)->dict: