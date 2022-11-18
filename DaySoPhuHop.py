t = int(input())
for i in range(0,t):
    n = int(input())
    arr1 = sorted([int(x) for x in input().strip().split()])
    arr2 = sorted([int(x) for x in input().strip().split()])
    check = True
    for i in range(0,n):
        if arr1[i] > arr2[i]:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")