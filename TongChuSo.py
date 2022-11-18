def sum(s):
    res = 0
    index = 0
    if s[0] == "-":
        res+= ord('-') - ord('0')
        index +=1
    for i in range(index,len(s)):
        res += int(s[i])
    return str(res)

number = input()
cnt = 0
while(len(number) > 1):
    number = sum(number)
    cnt+=1
print(cnt)
