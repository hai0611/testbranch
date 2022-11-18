t = int(input())
for i in range(0,t):
    n,d = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    for i in range(d,n):
        print(arr[i],end=" ")
    for i in range(0,d):
        print(arr[i],end=" ")
    print()