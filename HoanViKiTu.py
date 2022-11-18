s = input()
s = "0"+s
check = [0]*1000
n = len(s)-1
arr = [0]*1000
def Try(i):
    for j in range(1,n+1):
        if check[j] == 0:
            arr[i] = j
            check[j] = 1
            if i == n:
                for i in range(1,n+1):
                    print(s[arr[i]],end="")
                print()
            else:
                Try(i+1)
            check[j] = 0
Try(1)
