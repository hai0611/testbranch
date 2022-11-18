t = int(input())
for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr1 = list(set(arr))
    for i in arr1:
        if arr.count(i) % 2 != 0:
            print(i)
            break
    

