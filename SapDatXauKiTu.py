def check(s1,s2):
    l1 = [x for x in s1]
    l2 = [x for x in s2]
    if len(l1) != len(l2):
        return False
    l1.sort()
    l2.sort()
    for i in range(0,len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

t = int(input())
l = list()
cnt = 1
for i in range(0,t):
    s1 = input()
    s2 = input()
    res =""
    if check(s1,s2):
        res+="Test "+str(i+1)+": YES"
    else:
        res+="Test "+str(i+1)+": NO"
    l.append(res)
for i in l:
    print(i)

