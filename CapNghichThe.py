t = int(input())
arr = [int(x) for x in input().strip().split()]
cnt = 0
for i in range(0,t):
    for j in range(i+1,t):
        if i < j and arr[i] > arr[j]:
            cnt+=1
print(cnt)