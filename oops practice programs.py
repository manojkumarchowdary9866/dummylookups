
'''
#static method
class bank:
    def __init__(self,name,bal,pin):
        self.name=name
        self.bal=bal
        self.pin=pin
    def withdraw(self,n):
        if self.pin==bank.PIN():
            if self.bal>=n:
                self.bal-=n
                print("withdraw successfully!!!!!!!!")
                print(f'available bal is {self.bal}')
            else:
                print("insufficient bal")
        else:
            print("incorrect pin")
    @staticmethod
    def PIN():
        password=int(input("enter yout pin: "))
        return password
ob=bank("manoj",98658,9866)
ob1=bank("seshu",85563,9874)
ob.withdraw(1000)
ob1.withdraw(10000)

#staticmethod
class sample:
    @staticmethod
    def add(x,y):
        print(x+y)
    @staticmethod
    def sub(x,y):
        print(x-y)
ob=sample()
ob.add(20,30)
sample.sub(50,20)





#classmethod
class animal:
    place='forest'
    def __init__(self,name):
        self.name=name
        print("object is created")
    @classmethod
    def sample(cls):
        print(cls.place)
    @classmethod
    def modify(cls,newplace):
        cls.place=newplace
ob=animal("lion")
ob1=animal("deer")
animal.sample()
ob.sample()
animal.modify('tiger')
animal.sample()
ob1.sample()


#singleton class example
def o(arg):
    print(f'arg:{arg}')
    d={}
    def inn():
        if len(d)==0:
            d[arg]=arg()
        return d[arg]
    return inn
@o
class movie:
    def __init__(self):
        self.tickets=100
    def booking(self,n):
        if self.tickets>=n:
            self.tickets-=n
            print(f"{n} booking successfully!! ")
            print(f'available tickets is {self.tickets}')
        else:
            print(f'{n} tickets not available')





def bookmyshow():
    obj=movie()
    n=int(input("enter your tickets: "))
    obj.booking(n)

bookmyshow()
bookmyshow()
bookmyshow()
bookmyshow()
bookmyshow()
bookmyshow()
bookmyshow()
bookmyshow()
bookmyshow()



#singleton class
def o(arg):
    print(f'arg:{arg}')
    d={}
    def inn():
        if len(d)==0:
            d[arg]=arg()
        return d[arg]
    return inn
@o
class a:
    def __init__(self):
        print("object is created")
var=a()
print(var)
var1=a()
print(var1)
var2=a()
print(var2)
#output #same object address
arg:<class '__main__.a'>
object is created
<__main__.a object at 0x00000286A2122DD0>
<__main__.a object at 0x00000286A2122DD0>
<__main__.a object at 0x00000286A2122DD0>


def o(arg):
    print(f'arg:{arg}')
    def inn():
        x=arg()
        return x
    return inn
@o
class a:
    def __init__(self):
        print("object is created")
var=a()
print(var)
var1=a()
print(var1)
var2=a()
print(var2)
#output difirent object address
arg:<class '__main__.a'>
object is created
<__main__.a object at 0x0000020D823D2B60>
object is created
<__main__.a object at 0x0000020D823D2DD0>
object is created
<__main__.a object at 0x0000020D823D2B30>


class a:
    def __init__(self):
        print("obje")
var=a
a()
var()
print(a)
print(var)

import time
def out(func):
    def inn():
        strattime=time.time()
        func()
        endtime=time.time()
        print(f"total time:{endtime-strattime}")
        
    return inn
@out
def add():
    t=0
    for i in range(1,100):
        t+=i
    print(t)
add()

@out
def fact():
    t=1
    for i in range(1,6):
        t*=i
    print(t)
fact()



def out(func):
    def inn(*args,**kwargs):
        a=func(*args,**kwargs)
        return a
    return inn
@out
def a(x,y):
    return x+y
x,y=5,6
u=a(x,y)
print(u)



#object method
class complexnumber:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def get_data(self):
        print(f'{self.real}+{self.imag}j')
num=complexnumber(10,20)
num.get_data()
num1=complexnumber(20)
num1.attr=10#creat attribute for num1
print((num1.real,num1.imag,num1.attr))
print(num.attr)#attribute error
'''
