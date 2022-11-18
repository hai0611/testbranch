from math import gcd


t = int(input())
for i in range(0,t):
    n1 = input()
    n2 = n1[::-1]
    if(gcd(int(n1),int(n2)) == 1):
        print("YES")
    else:
        print("NO")