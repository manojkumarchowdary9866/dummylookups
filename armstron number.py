n=153
c=n
count=len(str(n))
t=0
while n>0:
    t+=(n%10)**(count)
    n//=10
if c==t:
    print("armstrong number")
else:
    print("not")
