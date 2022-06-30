def f(n):
    if n==1 or n==2:
        return n
    return f(n-1)+f(n-2)
d={}
for i in range(1,27):
    x=f(i)
    for j in range(1,27):
        d[chr(i+64)]=x
print(d)
s="mnc"
s=s.upper()
for i in d:
    t=0
    for j in s:
        t+=d[j]
print(t)


def hai(S):
    d={'A':1,'B':2}
    for i in range(67,91):
        d[chr(i)]=d[chr(i-1)]+d[chr(i-2)]
    summ=0
    for i in S:
        summ+=d[i]
    print(summ)
        
hai('MNC')
        
