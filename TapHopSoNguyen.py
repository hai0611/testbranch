[n,m]= [int(x) for x in input().split()]
a = sorted(list(set([int(x) for x in input().split()])))
b = sorted(list(set([int(x) for x in input().split()])))
d = dict()
for i in a:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i]+=1
for i in b:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i]+=1
for (i,j) in d.items():
    if j == 2:
        print(i,end=" ")
print()
for i in a:
    if d[i] == 1:
        print(i,end=" ")
print()
for i in b:
    if d[i] == 1:
        print(i,end=" ")

