arr = list()
while len(arr) < 10:
    arr += [int(x) % 42 for x in input().strip().split()]
print(len(set(arr)))
