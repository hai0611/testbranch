t = int(input())
for i in range(0,t):
    n = int(input())
    arr = sorted([int(x) for x in input().split()])
    cnt = 0
    for i in range(0,n):
        l = i+1
        r = n-1
        while l<r:
            if arr[i] + arr[l] + arr[r] > 0: 
                r-=1
            elif arr[i] + arr[l] + arr[r] < 0:
                l+=1
            else:
                cnt+=1
                l+=1
    print(cnt)