import time
def outer(arg):
    def inner():
        starttime=time.time()
        print("*"*20)
        arg()
        print("*"*20)
        endtime=time.time()
        print(f'time: {endtime-starttime}')
    return inner
@outer
def add():
    start=int(input("tsart: "))
    end=int(input("end: "))
    t=0
    for i in range(start,end+1):
        t+=i
    print(t)
add()
@outer
def fact():
   n=int(input("n: "))
   fact=1
   for i in range(1,n+1):
       fact*=i

   print(fact)
fact()
