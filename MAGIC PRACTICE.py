'''from abc import ABC,abstractmethod
class jspider(ABC):
    def teaching(self):
        pass
class raveesh(jspider):
    def teaching(self):
        print("java")
        print("python")
class harshad(jspider):
    def teaching(self):
        print("python")
        print("django")
class kishore(jspider):
    def teaching(self):
        print("web technology")
        print("mern stuck")
ob=raveesh()
ob.teaching()


class humans(ABC):
    @abstractmethod
    def speaking(self):
        print("telugu")
class india(humans):
    def speaking(self):
        super().speaking()
        print("english")
    
ob=india()
ob.speaking()'''



'''class b:
    def __init__(self,x):
        self.x=x
    def __str__(self):
        return 'str is executed'
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
        
ob=b(100)
ob1=b(10)
print(ob<=ob1)
'''
