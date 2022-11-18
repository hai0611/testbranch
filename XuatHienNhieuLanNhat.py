t = int(input())
for i in range(0,t):
    n = int(input())
    d = dict()
    arr = [int(x) for x in input().split()]
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    maxValue = max(d.values())
    check = True
    for i,j in d.items():
        if j == maxValue and j > n//2:
            print(i)
            check = False
            break
    if check:
        print("NO")