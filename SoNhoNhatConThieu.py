n = int(input())
arr = list(set([int(x) for x in input().split()]))
check = True
for i in range(1,n):
    if arr[i] != arr[i-1]+1:
        print(arr[i-1]+1)
        check = False
        break
if check:
    print(max(arr)+1)