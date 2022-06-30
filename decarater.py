def outer():
    print('line 1')
    def inner():
        print("line 2")
    print("line 3")
    return inner#inner function address will  be return

x=outer()#in a inner function address will be stored
x()#inner function call
print(x)# inner function address


