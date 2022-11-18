from math import sqrt
def checkNT(p):
    if p<2:
        return False
    else:
        for i in range(2, int(sqrt(p))+1):
            if p % i == 0:
                return False
        return True
def check(n):
    if not checkNT(n):
        return False
    if not checkNT(int(str(n)[::-1])): 
        return False
    n = str(n)
    for i in n:
        if not checkNT(int(i)):
            return False
    sum = 0 
    for i in n:
        sum+=int(i)
    if not checkNT(sum):
        return False
    return True
  
t = int(input())
for i in range(0,t):
    n = int(input())
    if check(n):
        print("Yes")
    else:
        print("No")
