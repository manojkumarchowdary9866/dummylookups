def count(s):
    t=0
    s=s.lower()
    for i in s:
        if not((i>='a' and i<='z') or (i>='0' and i<='9')):
            t+=1
    return t

x=count('beru74r8ue9[/.,/.94878q93.,.][)(*&^%$#')
print(x)
