 class a:
    def __init__(self,x):
        self.x=x
    def __str__(self):
        return "__str__ is called"
    def __add__(self,other):
        return self.x+other.x
    def __gt__(self,other):
        return self.x>other.x
    def __ge__(self,other):
        return self.x>=other.x
    def __lt__(self,other):
        return self.x<other.x
    def __le__(self,other):
        return self.x<=other.x
ob=a(200)
ob1=a(200)
print(ob<=ob1)
        
