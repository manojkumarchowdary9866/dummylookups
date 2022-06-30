'''class b:
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step

    def __iter__(self):
        return self
    def __next__(self):
        x=self.start
        if self.start==self.end:
            raise StopIteration
        self.start+=self.step
        return x
for i in b(10,0,-1):
    print(i)
        

def sum(n):
    for i in range(n+1):
        yield i*i
x=sum(5)
print(list(x))

t=(i*i for i in range(5))
x=iter(t)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
'''
def sq(s):
    for i in range(s+1):
        yield i*i
print(sq(5))
x=sq(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
