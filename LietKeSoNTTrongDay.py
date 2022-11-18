from math import sqrt

def checkNT(number):
    if number < 2:
        return False
    else:
        for i in range(2,int(sqrt(number))+1):
            if number % i == 0:
                return False
    return True
n = int(input())
arr = [int(x) for x in input().split()]
d = dict()
l = list()
for i in arr:
    if checkNT(i) and i not in l:
        l.append(i)
    if i not in d.keys():
        d[i] = 1
    else:
        d[i]+=1
for i in l:
    print("{0} {1}".format(i,d[i]))
