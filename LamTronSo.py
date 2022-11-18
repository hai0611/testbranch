t = int(input())
for i in range(0,t):
    number = input()
    tmp = int(number[-1])
    for i in range(len(number)-1,0,-1):
        if int(tmp) >=5:
            tmp = int(number[i-1])+1
        else:
            tmp = int(number[i-1])
    print(tmp*pow(10,len(number)-1))