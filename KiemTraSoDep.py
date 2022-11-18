from cmath import sqrt


def checkNT(x):
    if(x<2):
        return False
    else:
        for i in range(2,sqrt(x)):
            if(x % i == 0):
                return False
    return True
t = int(input())
for i in range(0,t):
    tmp = input()
    res = tmp[::-1]
    res1 = res[0:4:1]
    res3 = int(res1[::-1])
    if(checkNT(res3)):
        print("YES")
    else:
        print("NO")
    