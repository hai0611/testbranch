from math import factorial


def check(n):
    sum = 0
    arr = [int(i) for i in n]
    for i in arr:
        sum+= factorial(i)
    if str(sum) == n:
        return True
    return False
t = int(input())
for i in range(0,t):
    n = input()
    if check(n):
        print("Yes")
    else:
        print("No")