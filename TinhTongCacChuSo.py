t = int(input())
for i in range(0,t):
    s = input()
    sum = 0
    res=""
    for i in s:
        try:
            sum += int(i)
        except:
            res+=i
    l = [x for x in res]
    l.sort()
    for i in l:
        print(i,end="")
    print(sum)