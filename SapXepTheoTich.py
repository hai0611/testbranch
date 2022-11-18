def tich(n):
    n = str(n)
    res = 1
    for i in n:
        res*=int(i)
    return res
t = int(input())
for i in range(0,t):
    n = int(input())
    arr = sorted([int(x) for x in input().split()],key=lambda x:(tich(x),x))
    for i in arr:
        print(i,end=" ")
    print()