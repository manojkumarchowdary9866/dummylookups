'''
#hybrid
class bankv:
    bank='raja bank'
    def __init__(self,name,bal,mno):
        self.name=name
        self.bal=bal
        self.mno=mno
    def dsp(self):
        print(f'name  :{self.name}')
        print(f'bal   :{self.bal}')
        print(f'mno   :{self.mno}')
class bankv2(bankv):
    def __init__(self,name,bal,mno,gmail):
        bankv.__init__(self,name,bal,mno)
        self.gmail=gmail
    def dsp(self):
        super().dsp()
        print(f'gmail :{self.gmail}')
class bankv3(bankv):
    def __init__(self,name,bal,mno,pan):
        bankv.__init__(self,name,bal,mno)
        self.pan=pan
    def dsp(self):
        super().dsp()
        print(f'pan   :{self.pan}')
class bankv4(bankv3,bankv2):
    def __init__(self,name,bal,mno,gmail,pan,AAD):
        bankv2.__init__(self,name,bal,mno,gmail)
        bankv3.__init__(self,name,bal,mno,pan)
        self.AAD=AAD
    def dsp(self):
        super().dsp()
        print(f'AAD :{self.AAD}')

ob=bankv4('manoj',96321,7412589632,'manoj@gmail.com','H987G8K',228523642832)
ob.dsp()
#output
name  :manoj
bal   :96321
mno   :7412589632
gmail :manoj@gmail.com
pan   :H987G8K
AAD :228523642832

#multilevel inheritance
class bankv:
    bank='raja bank'
    def __init__(self,name,bal,mno):
        self.name=name
        self.bal=bal
        self.mno=mno
    def dsp(self):
        print(f'name  :{self.name}')
        print(f'bal   :{self.bal}')
        print(f'mno   :{self.mno}')
class bankv2(bankv):
    def __init__(self,name,bal,mno,gmail):
        super().__init__(name,bal,mno)
        self.gmail=gmail
    def dsp(self):
        super().dsp()
        print(f'gmail :{self.gmail}')
class bankv3(bankv2):
    def __init__(self,name,bal,mno,gmail,pan):
        super().__init__(name,bal,mno,gmail)
        self.pan=pan
    def dsp(self):
        super().dsp()
        print(f'pan   :{self.pan}')
ob=bankv3("manoj",9632,9638527415,'manoj@gmail.com','AN38JS82K')
ob.dsp()
#output
name  :manoj
bal   :9632
mno   :9638527415
gmail :manoj@gmail.com
pan   :AN38JS82K

#multiple inheritance
class p:
   def prop(self):
       print("dance")
class p2:
    def prop(self):
       print("coocking")
class c(p,p2):
    def prop(self):
       print("studying")
       p.prop(self)
       p2.prop(self)
       
oc=c()
oc.prop()
#output
#studying
#dance
#coocking


class p:
   def __init__(self):
       print("inside p")
class p2:
    def __init__(self):
       print("inside p2")
class p3:
    def __init__(self):
       print("inside p3")
class c(p2,p3,p):
    def __init__(self):
       print("inside c")
       p.__init__(self)
       p2.__init__(self)
       p3.__init__(self)
oc=c()


class p:
    x=10
    y=60
class p2:
    s=50
class p3:
xclass c(p,p2,p3):
    pass
oc=c()
print(oc.x,oc.y,oc.s)#50 60 50 


#herarical inheritance
class a:
    def __init__(self):
        print("inside class a")
class b(a):
    def __init__(self):
        print("inside class b")

class c(a):
    pass
ob=b()#inside class b
ob1=c()#inside class a



class a:
    x=50
    @classmethod
    def dsp(cls):
        print(f"inside class a:{cls}")
    @classmethod
    def dspA(cls):
        print(f"inside class a:{cls}")
class b(a):
    z=90
    @classmethod
    def dsp(cls):
        print(f"inside class b:{cls}")
    @classmethod
    def dspb(cls):
        print(f"inside class b:{cls}")
ob=a()
ob1=b()
ob.dsp()#inside class a:<class '__main__.a'>
ob.dspA()#inside class a:<class '__main__.a'>
#ob.dspB()#attributeerror
ob1.dsp()#inside class b:<class '__main__.b'>
ob1.dspA()#inside class a:<class '__main__.b'>
ob1.dspb()#inside class b:<class '__main__.b'>
a.dsp()#inside class a:<class '__main__.a'>
a.dspA()#inside class a:<class '__main__.a'>
#a.dspb()#attributeerror
b.dsp()#inside class b:<class '__main__.b'>
b.dspA()#inside class a:<class '__main__.b'>
b.dspb()#inside class b:<class '__main__.b'>



#method chaining
class a:
    x=50
    def dsp(self):
        print("inside class a")
class b(a):
    z=90
    def dsp(self):
        print("inside class b")
        a.dsp(self)
        super().dsp()
#ob=a()
ob1=b()
#ob.dsp()
ob1.dsp()


class a:
    x=50
    def dsp(self):
        print("inside class a")
class b(a):
    z=90
    def dsp(self):
        print("inside class b")
ob=a()
ob1=b()
ob.dsp()#inside class a
ob1.dsp()#inside class b



#constructer chaining
class bankv():
    bank='icici'
    def __init__(self,name,bal,mbn):
        self.name=name
        self.bal=bal
        self.mbn=mbn
    def dsp(self):
        print(f'name :{self.name}')
        print(f'bal  :{self.bal}')
        print(f'mbn  :{self.mbn}')
class bankv2(bankv):
    def __init__(self,name,bal,mbn,gmail):
        bankv.__init__(self,name,bal,mbn)
        self.gmail=gmail
    def dsp(self):
        super().dsp()
        print(f'gmail:{self.gmail}')
ob=bankv("manoj",9854,9638527411)
ob1=bankv2("manoj",9854,963852741,'manoj@gamil.com')
#ob.dsp()
ob1.dsp()




class a:
    x=10
    y=20
    def __init__(self,b,c):
        self.b=b
        self.c=c
class b(a):
    z=50
    def __init__(self,b,c,a):
        super().__init__(b,c)
        self.a=a
ob=a(10,20)
ob1=b(50,60,90)
print(ob.b)
print(ob.c)
#print(ob.a)#attribute error
print(ob1.b)
print(ob1.c)
print(ob1.a)



class a:
    x=10
    y=20
    def __init__(self,b,c):
        self.b=b
        self.c=c
class b(a):
    z=50
    def __init__(self,a):
        self.a=a
ob=a(10,20)
ob1=b(50)
print(ob.b)
print(ob.c)
#print(ob.a)#attribute error
#print(ob1.b)#attribute error
#print(ob1.c)#attribute error
print(ob1.a)



class a:
    x=10
    y=20
    def __init__(self):
        print("inside class a")
class b(a):
    z=50
    def __init__(self):
        print("inside class b")
#ob=a()
ob1=b()


class a:
    x=10
    y=20
    def __init__(self):
        print("inside class")
class b(a):
    z=50
ob=a()
ob1=b()



class a:
    x=10
    y=20
    def dsp(self):
        print("object is created")
class b(a):
    z=50
ob=a()
ob1=b()
ob.dsp()
ob1.dsp()
#output
object is created
object is created





class a:
    x=20
    y=50
class b(a):
    z=59
ob=a()
ob1=b()
print(ob.x)
print(ob.y)
print(a.x)
print(a.y)
#print(a.z)#attributeError
#print(ob.z)#attributeError
print(ob1.x)
print(ob1.y)
print(ob1.z)
print(b.x)
print(b.y)
print(b.z)
'''
