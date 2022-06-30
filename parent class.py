class a:
    def __init__(self,name,mno):
        self.name=name
        self.mno=mno
    def disp(self):
        print(f'name:{self.name}')
        print(f'name:{self.name}')

class b(a):
    def __init__(self,name,mno,pan):
        super().__init__(name,mno)
        self.pan=pan
    def disp(self):
        super().disp()
        print(f"pan:{self.pan}")
class c(b):
    def __init__(self,name,mno,pan,gmail):
        super().__init__(name,mno,pan)
        self.gmail=gmail
    def disp(self):
        super().disp()
        print(f"gmail:{self.gmail}")
class d(b):
    def __init__(self,name,mno,pan,adno):
        super().__init__(name,mno,pan)
        self.adno=adno
    def disp(self):
        super().disp()
        print(f"adno:{self.adno}")
    

       
ob1=d("manoj",7075866213,"sdff6564k",9638527415)
ob1.disp()
