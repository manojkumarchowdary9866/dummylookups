class a:
    x=30
    def disp(self):
        print('disp  in class a')
class b(a):
    y=50
    def disp(self):
        super().disp()
        print("disp in class b")
oa=a()
ob=b()
ob.disp()

'''class a:
    x=20
    @classmethod
    def dsp(self):
        print(f'dsp in class a:{a}')
    @classmethod
    def dspA(self):
        print(f'dspA in class a:{a}')
        
class b(a):
    x=20
    @classmethod
    def dsp(self):
        print(f'dsp in class a:{b}')
    @classmethod
    def dspB(self):
        print(f'dspA in class a:{b}')
oa=a()
ob=b()
a.dsp()
oa.dsp()
a.dspA()
oa.dspA()
#a.dspB()#error
#oa.dspB()#Error
b.dsp()
ob.dsp()
b.dspB()
ob.dspB()
b.dspA()
ob.dspA()

        



class a:
    x=20
    def dsp(self):
        print('dsp in class a')
class b(a):
    y=40
    def dsp(self):
        #a.dsp(self)
        super().dsp()
        print("dsp in class b")
oa=a()
ob=b()
ob.dsp()



class bankv1():
    bname='sbi'
    IFSC='sbi001'
    def __init__(self,name,mno,bal):
        self.name=name
        self.mno=mno
        self.bal=bal
    def dsp(self):
        print(f'name:{self.name}')
        print(f'mno:{self.mno}')
        print(f'bal:{self.bal}')

class bankv2(bankv1):
    def __init__(self,name,mno,bal,pan,AAdhar):
        super().__init__(name,mno,bal)
        self.pan=pan
        self.AAdhar=AAdhar
    def dsp(self):
        super().dsp()
        print(f'pan:{self.pan}')
        print(f'AAdhar:{self.AAdhar}')
        
#ob1=bankv1('kane',9638527412,10000)
ob2=bankv2('kane',9638527412,10000,'55S5SD4SD',228523642838)
#ob1.dsp()
ob2.dsp()

class p:
    x=10
    def __init__(self,a,b):
        self.a=a
        self.b=b


class c(p):
    y=50
    def __init__(self,a,b,c):
        self.c=c
        #p.__init__(self,a,b)
        super().__init__(a,b)
        
#ob1=p(100,200)
ob2=c(500,200,600)
print(ob2.a)
print(ob2.b)
print(ob2.c)'''

#constructer chaining
#classname.__init__(self,args)
#super().functionname()
