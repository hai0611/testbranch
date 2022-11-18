from math import sqrt

def checkNT(number):
    if number < 2:
        return False
    else:
        for i in range(2,int(sqrt(number))+1):
            if number % i == 0:
                return False
    return True
def check(s):
    for i in range(0,len(s)):
        if checkNT(int(i)):
            if checkNT(int(s[i])) == False:
                return False
        else:
            if checkNT(int(s[i])) == True:
                return False
    return True

t = int(input())
for i in range(0,t):
    number = input()
    if check(number):
        print("YES")
    else:
        print("NO")
