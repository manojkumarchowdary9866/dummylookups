def squre(n):
    
    for i in range(n+1):
        yield i*i
x=squre(5)
print(x)#<generator object squre at 0x000001AF3272F140>
print(next(x))#0
print(next(x))#1
print(next(x))#4
print(next(x))#9
print(next(x))#16
print(next(x))#24
print(next(x))#StopIteratio
