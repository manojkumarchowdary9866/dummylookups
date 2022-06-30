class a:
    def __init__(self,name):
        self.name=name
    def dsp(self):
        print(f"name:{self.name}")
class b(a):

    def __init__(self,name,mno):
        a.__init__(self,name)
        self.mno=mno
    def dsp(self):
        super().dsp()
        print(f"mno:{self.mno}")
class c(a):
    def __init__(self,name,age):
        a.__init__(self,name)
        self.age=age
    def dsp(self):
        super().dsp()
        print(f"age:{self.age}")
class d(c,b):
    def __init__(self,name,mno,age,bal):
        b.__init__(self,name,mno)
        c.__init__(self,name,age)
        self.bal=bal
    def dsp(self):
        super().dsp()
        print(f"bal:{self.bal}")
ob=d("manu",9866847308,24,160000)
ob.dsp()
    
