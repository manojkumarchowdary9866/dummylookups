class a:
    x=10
    def __init__(self,b,c):
        self.b=b
        self.c=c
class b(a):
    y=100

    def __init__(self,b,c,d):
        self.d=d
        super().__init__(b,c)
ob1=a(100,200)
ob2=b(101,1231,120)
print(f'b:{ob1.b}')
print(f'c:{ob1.c}')
#print(f'd:{ob1.d}')#error
print(f'b1:{ob2.b}')
print(f'c2:{ob2.c}')
print(f'd:{ob2.d}')

