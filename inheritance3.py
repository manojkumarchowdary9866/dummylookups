class a:
    x=10
    def __init__(self,b,c):
        self.b=b
        self.c=c
class b(a):
    y=100

    def __init__(self,d):
        self.d=d
ob1=a(100,200)
ob2=b(120)
print(f'b:{ob1.b}')
print(f'c:{ob1.c}')
#print(f'd:{ob1.d}')#error
#print(f'b1:{ob2.b}')#error
#print(f'c2:{ob2.c}')#error
print(f'd:{ob2.d}')
