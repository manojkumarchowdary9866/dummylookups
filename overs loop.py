'''start=1
end=20
for i in range(start,end+1):
    for j in range(1,7):
        print(f'over {i}  ball {j}')
    print()'''
'''l=[1,2,3,4,3,2,1]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
l=[1,1,2,3,4,3,2,1]
count=0
while count<len(l):
    count2=count+1
    while count2<len(l):
        if l[count]==l[count2]:
             l.pop(count2)
        else:
            count2+=1
    count+=1
print(l)
l=[2,4,5,66,7,1,4,56]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>=l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
class bank1():
    Bname="icic"
    def __init__(self,name,accno,bal):
        self.name=name
        self.accno=accno
        self.bal=bal
    def display(self):
        print(f'name   :{self.name}')
        print(f'accno  :{self.accno}')
        print(f'bal    :{self.bal}')

class bank2(bank1):
    def __init__(self,name,accno,bal,gmail):
        bank1.__init__(self,name,accno,bal)
        self.gmail=gmail
    def display(self):
        super().display()
        print(f'gamil  :{self.gmail}')
x=bank2("manoj",852963741,100,"gade.maonj@gmail.com")
x.display()
class sample():
    @staticmethod
    def sample1(a,b):
        print(a+b)
    @staticmethod
    def sub(x,y):
        print(x-y)
ob1=sample()
ob1.sample1(10,20)
sample.sub(200,30)'''



