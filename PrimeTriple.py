from math import sqrt


def checkNT(p):
    if p<2:
        return False
    else:
        for i in range(2, int(sqrt(p))+1):
            if p % i == 0:
                return False
        return True
t = int(input())
for i in range(0,t):
    n = int(input())
    cnt = 0
    for i in range(2,n-5):
        if checkNT(i) and checkNT(i+2) and checkNT(i+6):
            cnt+=1
        elif checkNT(i) and checkNT(i+4) and checkNT(i+6):
            cnt+=1
    print(cnt)

