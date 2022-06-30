from abc import ABC,abstractmethod
class jspider(ABC):
    @abstractmethod
    def teaching(self):
        pass
class raveesh(jspider):
    def teaching(self):
        print("java")
        print("python")
        print("sriping")
        print("advance java")
class santhosh(jspider):
    def teaching(self):
        
        print("python")
class kishore(jspider):
    def teaching(self):
        print("java")
        print('html')
        print("MERN")
ob=raveesh()
ob.teaching()
print("*"*20)
ob1=santhosh()
ob1.teaching()
print("*"*20)
ob2=kishore()
ob2.teaching()
