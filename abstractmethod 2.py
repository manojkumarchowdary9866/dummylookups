from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass
    def speaking(self):
        print("bow bow")
class dog(animal):
    def move(self):
        print("walking")
    def speaking(self):
        super().speaking()
        print("barking")
d=dog()
d.move()
d.speaking()

