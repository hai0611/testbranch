def convert2to10(n):
    l = len(n)
    res = 0
    for i in range(0,l):
        if n[i] == "1":
            res+=pow(2,l-i-1)
    return res
def convert10tob(n,b):
    n = int(n)
    res = ""
    while n > 0:
        tmp = n % b
        if int(tmp) > 9:
            tmp = chr(tmp+55) 
        res+=str(tmp)
        n//=b
    return res[::-1]
t = int(input())
for i in range(0,t):
    b = int(input())
    n = input()
    if b == 2:
        print(n)
    else:
        s1 = convert2to10(n)
        print(convert10tob(s1,b))

