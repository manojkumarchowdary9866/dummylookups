
'''
#composition
class address:
    def __init__(self,street,locality,city):
        self.street=street
        self.locality=locality
        self.city=city
class emp():
    def __init__(self,name,Id,aadhar):
        self.name=name
        self.Id=Id
        self.aadhar=aadhar
        self.addr=address("munekallu",'gayatridevi temple','bangalore')

    def dsp(self):
        print(f'name:{self.name}')
        print(f'ID:{self.Id}')
        print(f'aadhar:{self.aadhar}')
        print(f'street:{self.addr.street}')
        print(f'locality:{self.addr.locality}')
        print(f'city:{self.addr.city}')
        
ob1=emp("manoj",852,228523642838)
ob2=emp("raju",985,2255664455669)
add1=address("martha",'multiplex','hyd')
ob1.dsp()
ob2.dsp()
#output
name:manoj
ID:852
aadhar:228523642838
street:munekallu
locality:gayatridevi temple
city:bangalore
name:raju
ID:985
aadhar:2255664455669
street:munekallu
locality:gayatridevi temple
city:bangalore



#aggrigation
class address:
    def __init__(self,street,locality,city):
        self.street=street
        self.locality=locality
        self.city=city
class emp():
    def __init__(self,name,Id,aadhar,add):
        self.name=name
        self.Id=Id
        self.aadhar=aadhar
        self.addr=add
    def dsp(self):
        print(f'name:{self.name}')
        print(f'ID:{self.Id}')
        print(f'aadhar:{self.aadhar}')
        print(f'street:{self.addr.street}')
        print(f'locality:{self.addr.locality}')
        print(f'city:{self.addr.city}')
        
add=address("munekallu",'gayatridevi temple','bangalore')
ob1=emp("manoj",852,228523642838,add)
add1=address("martha",'multiplex','hyd')
ob2=emp("raju",985,2255664455669,add1)

ob1.dsp()
ob2.dsp()
#output
name:manoj
ID:852
aadhar:228523642838
street:munekallu
locality:gayatridevi temple
city:bangalore
name:raju
ID:985
aadhar:2255664455669
street:martha
locality:multiplex
city:hyd



What is Polymorphism: The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.



#overloading /polymorphisim
class a:
    def sum(self,a=0,b=0,c=0):
        return a+b+c
ob=a()
print(ob.sum(10,20))#30
print(ob.sum(20,30,40))#90
print(ob.sum(10))#10


def sum(a,b):
    print(a+b)
def sum(a,b,c):
    print(a+b+c)
sum(10,20,30)#60
sum(10,20)#TypeError: sum() missing 1 required positional argument: 'c'

'''
