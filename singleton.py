def outer(arg):#address of class
    print(f'arg:{arg}')
    d={}
    def inner():
        if len(d)==0:
        
            d[arg]=arg()#decorated function call
        return d[arg]
    return inner#address of inner
@outer
class a():
    def __init__(self):
        print("object created")

ob1=a()#inner fuction call
ob2=a()
ob3=a()
print(ob1)
print(ob2)
print(ob3)
