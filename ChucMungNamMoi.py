t = int(input())
listLC = list()
for i in range(0,t):
    s = input().strip()
    listLC.append(s)
listLC = list(set(listLC))
print(len(listLC))
