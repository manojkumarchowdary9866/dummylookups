class a:
    bname="icici"
    @classmethod
    def display(cls):
        print(f'class in a:{cls}')
    @classmethod
    def displayA(cls):
        print(f'class in a:{cls}')
class b(a):
    @classmethod
    def display(cls):
        super().display()
        print(f'class in b:{cls}')
    @classmethod
    def displayb(cls):
        print(f'class in b:{cls}')
oa=a()
ob=b()
ob.display()
oa.display()
oa.displayA()
ob.displayb()
