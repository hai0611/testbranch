t = int(input())
for i in range(0,t):
    a,b = [int(x) for x in input().split()]
    arr = [1]*100
    for i in range(3,100):
        arr[i] = arr[i-1]+arr[i-2]
    for i in range(a,b+1):
        print(arr[i],end=" ")
    print() 