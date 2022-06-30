def fib(n):
    f=0
    s=1
    for i in range(n):
        yield f
        t=f+s
        f,s=s,t
        
        
#a=int(input('a:'))   
print(list(fib(5)))
