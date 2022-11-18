n = int(input())
a = [float(x) for x in input().split()]
maxA = max(a)
minA = min(a)
sum = 0
for i in a:
    if i == minA or i == maxA:
        n-=1
    else:
        sum+=i

print("{0:.2f}".format(sum/n))

