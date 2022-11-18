n = int(input())
arr = [int(x) for x in input().split()]
i = 1
while(i < len(arr)):
    if n > 2 and (arr[i] + arr[i-1]) % 2 ==0:
        del(arr[i])
        del(arr[i-1])
        n = len(arr)
        if i > 1:
            i-=1
        continue
    i+=1
print(len(arr))



