t = int(input())
for i in range(0,t):
    tmp = input()
    check = True
    for x in tmp:
        if(x != "0" and x!= "1" and x != "2"):
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")