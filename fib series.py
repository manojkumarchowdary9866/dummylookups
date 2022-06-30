def fib(f):
    f1=0
    s=1
    if f==1 or f==2:
        return f-1
    for i in range(f-2):
        t=f1+s
        f1,s=s,t
    return t
s=10
for i in range(1,s+1):
    
    print(fib(i))
