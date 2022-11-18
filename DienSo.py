t = int(input())
for i in range(0,t):
    n = int(input())
    arr = sorted(list(set([int(x) for x in input().split()])))
    amin = arr[0]
    amax = arr[len(arr)-1]
    print(amax-amin+1-len(arr))
    
