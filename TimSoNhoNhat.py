t = int(input())
for i in range(0,t):
    s = input().lower()
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            s = s.replace(i,' ')
    l = [ int(x.strip()) for x in s.split()]
    l.sort()
    print(l[len(l)-1])
