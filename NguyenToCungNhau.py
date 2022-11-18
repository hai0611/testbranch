from math import gcd


def checkNTcungNhau(a,b):
    if(gcd(a,b) == 1):
        return True
    return False
[a,b] = input().split(" ")
minn = pow(10,int(b)-1)
maxx = pow(10,int(b))
cnt = 0
for i in range(minn,maxx):
    if(checkNTcungNhau(int(a),i)):
        print(i,end=' ')
        cnt+=1
        if(cnt == 10) :
            print()
            cnt = 0