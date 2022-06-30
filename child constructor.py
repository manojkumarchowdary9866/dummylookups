class a:
    x=10
    def __init__(self,name,bal,accno):
        self.name  = name
        self.bal   = bal
        self.accno =accno
    def display(self):
        print(f'name :{self.name }')
        print(f'bal  :{self.bal}')
        print(f'accno:{self.accno}')
class b(a):
    y=20
    def __init__(self,name,bal,accno,gmail):
        a.__init__(self,name,bal,accno)
        self.gmail=gmail
    def display(self):
        super().display()
        print(f'gmail:{self.gmail}')
ob=b("manoj",12000,96385241,"manoj@gmail.com")
ob.display()
