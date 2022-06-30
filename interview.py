
def even(n,n1):
    t=0
    for i in range(n,n1+1):
        n=i
        while n>0:
            rem=n%10
            t+=rem
            n//=10
    return t

n=int(input('n: '))
n1=int(input('n1: '))
x=even(n,n1)
print(x)
    
