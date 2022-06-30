n=15311
c=n
t=0
while n>0:
    t+=n%10
    n//=10
print(t)
if t%2==0:
    print('given number sum is even')
else:
    print('given number sum is even not')
    
