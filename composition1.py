class chiru:
    def __init__(self,m):
        self.m=m
    def __str__(self):
        return "__str__ is called"
    def __add__(self,other):
        return self.m+other.m
    def __sub__(self,other):
        return self.m-other.m
    def __gt__(self,other):
        return self.m>other.m
    def __ge__(self,other):
        return self.m>=other.m
    def __lt__(self,other):
        return self.m<other.m
    def __le__(self,other):
        return self.m<=other.m
ob=chiru(100)
ob1=chiru(100)
print(ob<=ob1)














'''class address():
    def __init__(self,street,locality,city):
        self.street=street
        self.locality=locality
        self.city=city
    
class employe():
    def __init__(self,name,Id,mob,addr):
        self.name=name
        self.Id=Id
        self.mob=mob
        self.adr=addr
    def dsp(self):
        print(f'name:{self.name}')
        print(f'Id:{self.Id}')
        print(f'Mob:{self.mob}')
        print(f'street:{self.adr.street}')
        print(f'locality:{self.adr.locality}')
        print(f'city:{self.adr.city}')
ob1=address('marthahalli','biryanizone','bangalore')
ob=employe('bala',125,963852741,ob1)
ob.dsp()
print("*"*20)

ob11=employe('mahi',126,8529637413,ob1)
ob11.dsp()

def man(a=0,b=0,c=0):
    return a+b+c
print(man())
print(man(10))
print(man(10,20))
print(man(10,20,30))
'''
