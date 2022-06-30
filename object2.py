def outer(arg):#address of class
    print(f'arg:{arg}')
    def inner():
        print("inside inner")
        x=arg()#decorated function call
        return x
    return inner#address of inner
@outer
class a():
    def __init__(self):
        print("object created")

ob1=a()#inner fuction call
