t = int(input())
for i in range(0,t):
    n = input()
    if n[0] == n[len(n)-1]:
        print("YES")
    else:
        print("NO")