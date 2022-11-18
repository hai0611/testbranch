t = int(input())
for i in range(0,t):
    s1,s2 = [int(x) for x in input().split()]
    p = str(max(s1,s2))
    q = str(min(s1,s2))    
    try:
        s = [x for x in input().split()]
        x1,x2 = s
    except:
        x1 = s[0]
        x2 = input()
    x11 = x1.replace(p,q)
    x12 = x2.replace(p,q)
    x21 = x1.replace(q,p)
    x22 = x2.replace(q,p)
    print("{0} {1}".format(int(x11)+int(x12),int(x21)+int(x22)))


