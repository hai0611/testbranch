n = int(input())
s1 = 0
s2 = 0
for i in range(0,n):
    arr = [int(x) for x in input().split()]
    s1 += sum(arr[0:i:])
    s2 += sum(arr[i+1::])
k = int(input())
if abs(s1 - s2) <= k:
    print("YES")
else:
    print("NO")
print(abs(s1-s2))
