def fib(n):
    f=0
    s=1
    if n==1 or n==2:
        return n-1
    for i in range(n-2):
        t=f+s
        f,s=s,t
    return t
n1=100
m=1
l=[]
while True:
    x=fib(m)
    if x>n1:
        break
    l.append(x)
    m+=1
print(l)

    
