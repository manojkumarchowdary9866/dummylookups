n=input("n: ").split()
x=list(map(lambda d:int(d),n))
t=0
for i in x:
    t+=i
if t%2==0:
    print(t)
else:
    t-=x[0]
    print(t)
    

