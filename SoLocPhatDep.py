def check(s):
    s = str(s)
    for i in s:
        if i !="6" and i !="8":
            return False
    if s == "8" or s =="88" or s =="86" or s.count("888") > 0:
        return False
    return True
s = input()
if check(s):
    print("YES")
else:
     print("NO")

