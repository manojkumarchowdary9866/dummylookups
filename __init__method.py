def bank():
    Bname="GMKC"
    IFSC ="GMKC00007"
    NOB  =50

    def __init__(self,Name,Acno,Mno):
        self.name=Name
        self.acno=Acno
        self.mno =Mno


ob1=bank("manoj",097310100075898,98668473080)
ob2=bank("depakraj",097310100078596,8529637410)
print(ob1.__dict__)
print(ob2.__dict__)
