class bank:
    Bname='hdfc'
    IFSC='hdfc0007'
    nob=50
    def __init__(self,name,acno,bal):
        self.name=name
        self.acno=acno
        self.bal=bal
        print(name,acno,bal)
        


ob1=bank('manoj',96385207415,10000)
ob2=bank('raj',98524525525,100225)
ob3=bank('prabha',968525201052,102255)
