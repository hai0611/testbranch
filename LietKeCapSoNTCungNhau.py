from math import gcd


n = int(input())
arr = sorted([int(x) for x in input().split()])
for i in range(0,n):
    for j in range(i+1,n):
        if gcd(arr[i],arr[j]) == 1:
            print("{0} {1}".format(arr[i],arr[j]))