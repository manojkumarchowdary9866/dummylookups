'''def outer(arg):#address of abc
    print("entering outer function")
    print(f'arg:{arg}')
    def inner():
        print("entering inner function")
        arg()#abc function callS
        print("exit inner function")
        
    print("exit outer function")
    return inner
    
    

@outer
def abc():#address of inner function 
    print("abc excute")
print(f'abc:{abc}')
abc()#inner function call'''
def outer(arg):
    def inner():
        print("*"*20)
        arg(9,5)
        print("*"*20)


    return inner
@outer
def add(x,y):
    print(x*y)
    print(x)

add()



