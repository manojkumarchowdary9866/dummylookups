from abc import ABC,abstractmethod
class jspider(ABC):
    @abstractmethod
    def teaching(self):
        pass
class raveesh(jspider):
    def teaching(self):
        print("java")
class santhosh(jspider):
    def teaching(self):
        print("python")


class manjunath(jspider):
    def teaching(self):
        print("java")
        print("jee2")
        print("sql")
#a=santhosh()
#a=raveesh()
a=manjunath()
a.teaching()
