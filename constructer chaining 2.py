class bank:
    Bname="icici"
    def __init__(self,name,acno,bal):
        self.name=name
        self.acno=acno
        self.bal=bal
    def display(self):
        print(f'name :{self.name}')
        print(f'acno :{self.acno}')
        print(f'bal  :{self.bal}')
class bank2(bank):
    def __init__(self,name,acno,bal,gamail):
        bank.__init__(self,name,acno,bal)
        self.gmail=gamail

    def display(self):
        super().display()
        print(f'gamil:{self.gmail}')
ob1=bank2("manoj",963852147,40000,"gade.manoj@gmail.com")
ob1.display()
