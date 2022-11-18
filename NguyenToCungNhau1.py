from math import gcd

def checkNTcungNhau(a,b):
    if(gcd(a,b) == 1):
        return True
    return False
n = int(input())
arr = sorted([int(x) for x in input().split()])
for i in range(0,n):
    for k in range(i+1,n):
        if checkNTcungNhau(arr[i],arr[k]):
            print("{0} {1}".format(arr[i],arr[k]))
