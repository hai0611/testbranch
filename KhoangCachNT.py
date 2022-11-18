from math import sqrt


def checkNT(s):
    if s<2:
        return False
    else:
        for i in range(2,int(sqrt(s))+1):
            if s % i == 0:
                return False
        return True
n,x = [int(s) for s in input().strip().split()]
l = list()
cnt = 0
z = 2
while cnt < n:
    if checkNT(z):
        l.append(z)
        cnt+=1
    z+=1
print(x,end=" ")
for i in l:
    x+=i
    print(x,end=" ")


