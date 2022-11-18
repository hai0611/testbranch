from re import S


s1 = set([x.strip() for x in input().lower().split()])
s2 = set([x.strip() for x in input().lower().split()])
hop = set()
giao = set()
for i in s1:
    hop.add(i)
    if i in s2:
        giao.add(i)
for i in s2:
    hop.add(i)
s = list(hop)
s.sort()
sp = list(giao)
sp.sort()
for i in s:
    print(i,end=" ")
print()
for i in sp:
    print(i,end=" ")