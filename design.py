def decorator(arg):#carry address of decarated function
    def inner():
        print("*"*20)
        arg()#decarated function call not ginen 

        
        print("*"*20)
    return inner
@decorator
def add(b,y):# stored inner function address
    print("am first texter")
add()#inner function call

@decorator
def text():
    print("am second texter")
text()
 
