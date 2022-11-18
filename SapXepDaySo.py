t = int(input())
for i in range(0,t):
    [n,m] = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    amax = sorted(arr)[len(arr)-1]
    res = list()
    for i in arr:
        if i == amax:
            res.append(m)
        res.append(i)
    for i in res:
        if i<0:
            print(i,end=" ")
    for i in res:
        if i>=0:
            print(i,end=" ")
    print()