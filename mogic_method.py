class A:
    def __init__(self,x):
        self.x=x
    def __str__(self):
        return '__str__ is called'
    def __add__(self,other):
        return self.x+other.x
    def __gt__(self,other):
        if self.x>other.x:
            return f'{self.x} is greater'
        return f'{other.x} is greater'
    def __ge__(self,other):
        return self.x>=other.x
    def __lt__(self,other):
        return self.x<other.x
    def __le__(self,other):
        return self.x<=other.x
    
ob1=A(1000)
#print(ob.x)
ob2=A(1000)
print(ob1>=ob2)
