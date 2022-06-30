def fib(n):
    f=0
    s=1
    yield 0
    yield 1
    for i in range(n-2):
        t=f+s
        f,s=s,t
        yield t
l=[]
for i in fib(10):
    l.append(i)
print(l)
