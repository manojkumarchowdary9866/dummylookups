class a():
    def __init__(self,name):
        self.name=name
    def disp(self):
        print(f"name={self.name}")
class b(a):
    def __init__(self,name,mno):
        super().__init__(name)
        self.mno=mno
    def disp(self):
        super().disp()
        print(f"mno={self.mno}")
class c(a):
    def __init__(self,name,bal):
        super().__init__(name)
        self.bal=bal
    def disp(self):
        super().disp()
        print(f"bal={self.bal}")
class c2(b,c):
    def __init__(self,name,mno,bal,adno):
        b.__init__(self,name,mno)
        c.__init__(self,name,bal)
        self.adno=adno
    def disp(self):
        b.disp(self)
        c.disp(self)
        print(f"adno={self.adno}")
ob=c("manoj",963852741,1000,228523642838)
ob.disp()
    
