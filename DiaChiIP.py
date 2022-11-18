t = int(input())
for i in range(0,t):
    try:
        s = [int(x) for x in input().split(".")]
    except:
        print("NO")
        continue
    check = True
    for n in s:
        if len(s) != 4 or n < 0 or n > 255:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")

