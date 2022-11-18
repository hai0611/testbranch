from math import sqrt

def checkNT(s):
    if s<2: 
        return False
    else:
        for i in range(2,int(sqrt(s))+1):
            if s % i ==0:
                return False
        return True
[n,m] = [int(x) for x in input().split()]
l = list()
for i in range(0,n):
    l.append([1 if checkNT(int(x)) else 0 for x in input().split()])
for i in l:
    print(*i)
        


