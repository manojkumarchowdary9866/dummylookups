import time
def decorator(arg):
    def inner():
        starttime=time.time()
        arg()
        endtime=time.time()
        print(f' time taken:{endtime-starttime}')
    return inner
@decorator
def add():
    start=int(input())
    end=int(input())
    t=0
    for i in range(start,end+1):
        t+=i
    print(i)
add()
@decorator
def fact():
    fact=1
    n=int(input())
    for i in range(1,n+1):
        fact*=i
    print(f' facotial of :{fact}')
fact()
    
        
