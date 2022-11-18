from math import gcd


t = int(input())
for i in range(0,t):
    n1 = input()
    n2 = input()
    print(gcd(int(n1),int(n2)))