from math import sqrt
def checkNT(p):
    if p<2:
        return False
    else:
        for i in range(2, int(sqrt(p))+1):
            if p % i == 0:
                return False
        return True
def check(s):
    if s == s[::-1]:
        return False
    if checkNT(int(s)) and checkNT(int(s[::-1])):
        return True
    return False
t = int(input())
for i in range(0,t):
    checkNumber = [0]*1000005
    n = int(input())
    for i in range(10,n):
        if checkNumber[i] == 0:
            tmp = str(i)
            if check(tmp) and int(tmp[::-1]) < n:
                print("{0} {1}".format(tmp,tmp[::-1]),end=" ")
                checkNumber[int(tmp)] = 1
                checkNumber[int(tmp[::-1])] = 1
    print()
