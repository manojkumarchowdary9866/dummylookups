class a:
    x=10
    def display(self):
        print("display class a")
class b(a):
    y=100
ob1=a()
ob2=b()
ob1.display()
ob2.display()
