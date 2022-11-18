from math import sqrt


def nt(s):
    if s[0] != "#":
        return False
    if s[len(s)-1] =="&":
        return False
    if s[1] =="$" and s[len(s)-1] !="$":
        return False
    cnt = 0
    for i in s:
        if i == "#":
            cnt+=1
    if cnt != 1:
        return False
    cnt1 = 0
    if s[len(s)-1] =="*":
        for i in s:
            if i == "&":
                cnt+=1
        if cnt == 0:
             return False
    return True

s1 = "#%%$"
s2 = "#&#&"
s3 = "#$$%"
s4 = "#%**"
s5 = "&#%*"
print(nt(s1))
print(nt(s2))
print(nt(s3))
print(nt(s4))
print(nt(s5))