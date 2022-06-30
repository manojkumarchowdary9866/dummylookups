class a:
    def __init__(self,x):
        self.x=x
    def __str__(self):
        return '__str__ is called'
    def __add__(self,other):
        return self.x+other.x
    def __gt__(self,other):
        return self.x>other.x
ob=a(100)
ob1=a(10)
print(ob>ob1)
