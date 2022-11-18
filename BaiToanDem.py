t = int(input())
l = list()
while(True):
    l.extend([int(x) for x in input().split()])
    if len(l) == t:
        break
r = sorted(l)[len(l)-1]
check = True
for i in range(1,r+1):
    if i not in l:
        print(i)
        check = False
if check:
    print("Excellent!")
#ahihiii