class a():
    @classmethod
    def disp(cls):
        print(f'inside class:{cls}')
    @classmethod
    def dispA(cls):
        print(f'inside class:{cls}')
class b(a):
    @classmethod
    def disp(cls):
        print(f'inside class:{cls}')
    @classmethod
    def dispb(cls):
        print(f'inside class:{cls}')
ob=a()
ob1=b()
ob.disp()
ob1.disp()
ob.dispA()
ob1.dispA()
#ob.dispb()#error
ob1.dispb()
a.disp()
b.disp()
a.dispA()
b.dispb()
