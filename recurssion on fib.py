#recurssion on fib
def fib(s):
    if s==1 or s==2:
        return s-1
    return fib(s-1)+fib(s-2)



x=fib(10)
print(f'fib:{x}')
'''
                   fib(6)
                   (5)
            fib(5) + fib(4)
            (3)    +  (2)
        fib(4)+fib(3)                 fib(3)+fib(2)
         (2)  + (1)                    (1)+(1)
    fib(3)+fib(2) fib(2)+fib(1)      fib(2)
     (1)+1        (1)+(0)
fib(2)+fib(1)
   (1) +       (0)'''

