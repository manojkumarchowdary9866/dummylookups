class bankv:
    name='icici'
    IFSC='icici0007'
    def __init__(self,name,acno,bal):
        self.name=name
        self.acno=acno
        self.bal=bal
    def dsp(self):
        print(f"name  :{self.name}")
        print(f"acno  :{self.acno}")
        print(f"bal   :{self.bal}")
class bankv2(bankv):
    def __init__(self,name,acno,bal,aadhar):
        bankv.__init__(self,name,acno,bal)
        self.aadhar=aadhar
    def dsp(self):
        super().dsp()
        print(f'aadhar:{self.aadhar}')
class bankv3(bankv):
    def __init__(self,name,acno,bal,gmail):
        bankv.__init__(self,name,acno,bal)
        self.gmail=gmail
    def dsp(self):
        super().dsp()
        print(f'gmail:{self.gmail}')
class bankv4(bankv3,bankv2):
    def __init__(self,name,acno,bal,aadhar,gmail,pan):
        bankv2.__init__(self,name,acno,bal,aadhar)
        bankv3.__init__(self,name,acno,bal,gmail)
        self.pan=pan
    def dsp(self):
        super().dsp()
        print(f'pan  :{self.pan}')

ob2=bankv("mahesh",97310100075898,69855)
ob2.dsp()
print("*"*20)
    
ob=bankv2("ntr",9710100075898,654123,228523642838)
ob.dsp()
print('*'*20)
ob1=bankv3('balayya',96385274112,65463,'balayya@gmail.com')
ob1.dsp()


print('*'*20)
ob3=bankv4('pal',963258741235,6586,321456987412,'pal@gmail.com','AM56A7K')
ob3.dsp()




























'''l= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
       
result=[]
temp=max(l, key=lambda x: x[1])

largest, larger = temp[1], temp[1]
for num in l:
    if num[1] < largest:
        largest, larger = num[1], largest
    elif num[1] < larger:
        larger = num[1]
        result.append(larger)
print(result)
#lst=[['Prashant',36],['Pallavi',36],['Dheeraj',39],['Shivam',40]]
lst=[['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]]
names=[]
lowest = lst[0].__getitem__(1)
second_lowest=0
for l in lst:
    if l[1] < lowest:
        second_lowest = lowest
        lowest = l[1]
    elif l[1]<=second_lowest:
        second_lowest=l[1]
        print(lst)
for l in lst:
    if l[1]==second_lowest:
        names.append(l[0])

for i in range(len(names)):
    if i==2:
        break
    print(names[i])
    
'''


