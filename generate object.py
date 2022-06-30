def Sum(n):
    for i in range(n+1):
        yield i
        yield 'a'
x=Sum(5)
print(x)
print(list(x))


'''t=(i*i for i in range(5))
print(t)
x=iter(t)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
'''
