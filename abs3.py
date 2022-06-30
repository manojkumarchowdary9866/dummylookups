from abc import ABC,abstractmethod
class college(ABC):
    @abstractmethod
    def stream(self):
        pass
class degree(college):
    def stream(self):
        print("electronics")
class btech(college):
    def stream(self):
        print('civil')
        print("cs")
ob=degree()
ob.stream()
ob1=btech()
ob1.stream()

'''class animal(ABC):
    @abstractmethod
    def move(self):
        pass
    def speaking(self):
        print('bow bow')

class dog(animal):
    def move(self):
        print('walking')
    def speaking(self):
        super().speaking()
        print("barking")
class snake(animal):
    def move(self):
        print('crwal')
ob=dog()
ob.speaking()
print('snake')
ob1=snake()
ob1.move()'''
