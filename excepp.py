

    
    






'''
from math import factorial
def fact(n):
    if n==0 or n==1:
        return 
    return n*fact(n-1)
try:
    assert fact(5)==factorial(5),'wrong'

    
except AssertionError as m:
    print(m)

class pri(Exception):
   def __str__(self_):
       return 'magic method executed'
try:
    n=eval(input("n: "))
    for i in range(2,n//2+1):
          if n%i==0:
              raise pri('not prime')
except pri as msg:
    print(msg)
else:
    print("prime number")
          




try:
    #riskycode
    a=int(input('a: '))
    b=int(input('b: '))
    if b==0:
        try:
            b=int(input("enter value >0: "))
           
        except ZeroDivisionError as msg:
            print(msg)
except ValueError as msg:
    print(msg)
else:
    print(a/b)
finally:
    print("finally block execute")





try:
    #code
    a=int(input("a: "))
    b=int(input("b: "))
    c=a//b

except:
    print("except block execute")
else:
    print(c)
finally:
    print("finally block execute")




l=[9,20,60,80,90]
a=3
try:
    for i in range(len(l)):
        print(l[a])
        a+=1
except ZeroDivisionError as msg:
    print(msg)
except IndexError as msg:
    print(msg)
except:
    print("inside except block")
'''
