full=lambda fn,sn:fn+sn
x=full("manoj",'gade')
print(x)


mul=lambda a,b,c:a*b*c
x=mul(10,20,60)
print(x)


def mul(s):
    return s*10
l=[10,20,30]
m=list(map(mul,l))
print(m)


m1=list(map(lambda x:x*20,l))
print(m1)

k=[5,6,8,4,3,9]
f=list(filter(lambda g:g%2==0,k))
print(f)
