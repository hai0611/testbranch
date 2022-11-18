from math import sqrt


def checkNT(s):
    s = int(s)
    if s < 2:
        return False
    else:
        for i in range(2, int(sqrt(s))+1):
            if s % i == 0:
                return False
        return True
def check1(s):
    if checkNT(len(s)) == False:
        return False
    nt = 0
    knt = 0
    for i in s:
        if checkNT(i):
            nt+=1
        else:
            knt+=1
    if nt<=knt:
        return False
    return True
t = int(input())
for i in range(0,t):
    s = input()
    if check1(s):
        print("YES")
    else:
        print("NO")
    

