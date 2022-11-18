t = int(input())
for i in range(0,t):
    n = int(input())
    arr = [0]*n
    d = dict()
    for j in range(0,n):
        x = int(input())
        if x not in d:
            d[x] = 1
        else:
            d[x]+=1
    maxValue = max([x for x in d.values()])
    l = list()
    for i,j in d.items():
        if j == maxValue:
            l.append(i)
    l.sort()
    print(l[0])
