def fib(n):#0 1 1 2
    f=0
    s=1
    if n==1 or n==2:
        return n-1
    for i in range(n-2):
        t=f+s
        f,s=s,t
    return t
n1=
for i in range(1,n1+1):
    print(fib(i), end=" ")
