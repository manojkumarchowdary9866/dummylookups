def outer(arg):#address of class
    print(f'arg:{arg}')
    d={}
    def inner():
        d[arg]=arg()#decorated function call and object creation
        return d[arg]
    return inner#address of inner
@outer
class a():#inner address store in classname(a)
    def __init__(self):
        print("object created")

ob1=a()#inner fuction call given with class name()
ob2=a()
ob3=a()
print(ob1)
print(ob2)
print(ob3)
