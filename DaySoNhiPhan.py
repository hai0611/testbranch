t = int(input())
arr = [int(x) for x in input().strip().split()]
cnt = 0
for i in range(1,t):
    if arr[i] != arr[i-1]:
        cnt+=1
print(cnt)
