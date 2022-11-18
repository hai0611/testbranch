while(True):
    arr = [int(x) for x in input().split()]
    if len(set(arr)) == 1 and arr[0] == 0:
        break
    cnt = 0
    while len(set(arr)) != 1:
        tmp = arr[0]
        arr[0] = abs(arr[0] - arr[1])
        arr[1] = abs(arr[1] - arr[2])
        arr[2] = abs(arr[2] - arr[3])
        arr[3] = abs(arr[3] - tmp)
        cnt+=1
    print(cnt)

