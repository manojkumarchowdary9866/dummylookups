class manu:
    def __init__(self):
        print("object created")
ob1=manu
b=ob1()
print(manu)
print(ob1)


'''import time
def dec(arg):
    def inner():
        startTime=time.time()
        arg()
        endTime=time.time()
        print(f'time taken:{endTime-startTime}')
        

    return inner
    

@dec
def add():
    f=10
    s=100
    t=0
    for i in range(f,s):
        t+=i
    print(t)
add()


@dec
def fact():
    n=6
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)
fact()'''




'''def out(arg):
    def inn(*args,**kwargs):
            a1=arg(*args,**kwargs)
            return a1       
    return inn
@out
def add(a,b):
    return a*b

print(add(6,9))


@out
def sub(m,n):
    return m-n
print(sub(6,3))'''
