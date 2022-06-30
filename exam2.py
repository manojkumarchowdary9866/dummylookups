'''def outer(arg):

    def inner():
        v=arg(5,6)
        return v
       
    return inner
@outer
def sample(a,b):
    return a+b

print(sample())
cannot be changed'''



n='12351'
c=n
t=''
for i in range(-1,-len(n)-1,-1):
    t=t+n[i]
if c==int(t):
    print('palindrome')
else:
    print("not")
    







    add
























def number(s):
    s=s.lower()
    
    n=""
    for i in s:
        if i>="0" and i<="9":
            n+=i
    return n

m=0
a=number("G@WS%$5673!9UB&NW,^S7234")
for i in a:
    m+=int(i)

