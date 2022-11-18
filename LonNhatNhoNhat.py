while(True):
    n = int(input())
    if n == 0:
        break
    else:
        l = list()
        for i in range(0,n):
            l.append(int(input()))
        if len(set(l)) == 1:
            print("BANG NHAU")
        else:
            l.sort()
            print("{0} {1}".format(l[0],l[len(l)-1]))