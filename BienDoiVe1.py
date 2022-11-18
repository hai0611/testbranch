while(True):
    n = int(input())
    cnt = set()
    cnt.add(n)
    if n == 0:
        break
    elif n == 1:
        print(1)
        continue
    while n != 1:
        if n % 2 == 0:
            n//=2
            cnt.add(n)
        else:
            n = n*3 +1
            cnt.add(n)
    print(len(cnt))
    