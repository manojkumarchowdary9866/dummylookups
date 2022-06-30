def upper(s):
    t=''
    for i in s:
        if i>='A' and i<='Z':
            t+=chr(ord(i)+32)
        if i>='a' and i<='z':
            t+=chr(ord(i)-32)
        else:
            t+=i
    return t
x=upper('WE ARE python DEVELOPERS')
print(x)
