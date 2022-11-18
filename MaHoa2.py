P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    x = input()
    if(x== "0"):
        break
        continue
    [k,s] = x.split(" ")
    res = ""
    for i in range(0,len(s)):
        res+=P[(P.find(s[i])+int(k))%28]
    print(res[::-1])