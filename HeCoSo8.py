def convert2(s):
    return str(int(s[0])*2*2 + int(s[1])*2 + int(s[2])*1)
s = input()
res =""
while(len(s) >= 3):
    res+= convert2(s[-3::])
    s = s[:-3:]
if len(s) == 1:
    s = "00"+s
    res+=convert2(s)
if len(s) == 2:
    s = "0"+s
    res+=convert2(s)
print(res[::-1])