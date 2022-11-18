n,k = [int(x) for x in input().split()]
arr1 = list(set([int(x) for x in input().split()]))
arr1.sort()
n = len(arr1)
arr = [x for x in range(1,n+1)]
OK = False
def inR():
    for i in range(0,k):
        print(arr1[arr[i]-1],end=" ")
def sinh():
    i = k-1
    while arr[i] == n-k+i+1:
        i-=1
    if i < 0:
        global OK 
        OK = True
    else:
        arr[i]+=1
        for j in range(i+1,k):
            arr[j] = arr[j-1]+1
while(not OK):
    inR()
    print()
    sinh()
    # arr1 = 1 2 3 4 5
    # arr = 3 4 5