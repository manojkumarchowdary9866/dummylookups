def Addig(s):
    if s==0:
        return 0
    return s%10+Addig(s//10)
x=Addig(85265)
print(x)

def fact(s):
    if s==0 or s==1:
        return 1
    return s*fact(s-1)
x=fact(7)
print(x)


def fib(s):
    if s==1 or s==2:
        return s-1
    return fib(s-1)+fib(s-2)
n=10
l=[]
for i in range(1,n+1):
    l.append(fib(i))
print(l)

def Prime(n, i = 2):
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):

        return True
 
    # Check for next divisor
    return Prime(n, i + 1)
 
 
# Driver Program
n = 19
if (Prime(n)):
    print("Yes")
else:
    print("No")
     
    
