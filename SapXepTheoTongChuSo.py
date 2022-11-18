def sumNumber(n):
    res = 0
    for i in n:
        res+=int(i)
    return res
t = int(input())
for i in range(0,t):
    n = int(input())
    arr =[int(x) for x in input().split()]
    d = dict()
    for i in arr:
        d[i] = sumNumber(str(i))
    sort_x = sorted(d.items(),key= lambda x:(x[1],int(x[0])))
    for i,j in sort_x:
        print(i,end=" ")
    print()
