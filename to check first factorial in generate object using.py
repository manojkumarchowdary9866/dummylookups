def fact(n):
    yield 1
    t=1
    for i in range(1,n+1):
        t*=i
        yield t
for i in fact(5):
    print(i)

'''
op
1
1
2
6
24
120'''
