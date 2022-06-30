
'''
from functools import reduce
l=[10,20,3,40,50]
x1=reduce(lambda x,y:x+y,l)
print(x1)



n=input().split()
m=list(map(int,n))
print(m)

l=[10,20,13,41,16,19]
f=list
m=list(map(lambda x:x%10==0,(filter(lambda x:x%2==0,l))))
print(m)


l=[10,20,13,41,16,19]
f=list(filter(lambda x:x%2==0,l))
print(f)

def mod(s):
    return s%2==0
l=[10,20,13,41,16,19]
f=list(filter(mod,l))
print(f)

l=[10,20,30,40]
m=list(map(lambda x:x*10,l))
print(m)



add=lambda x,y:x+y
x=add(10,20)
print(x)


p=['o','c','b','i']
v=[10,20,30,40]
d=dict(zip(p,v))
ps=['o','c','b']
vs=[10,20,30]
ds=dict(zip(ps,vs))
count=0
for i in ps:
    if d[i]==ds[i]:
        count+=1
print(count)

l=['xy','lk','po']
l2=['aa','bb',55]
d=dict(zip(l,l2))
l1={l[i]:l2[i] for i in range(len(l))}
print(l1)
print(d)


l=['xy','lk','po']
l2=['aa','bb']
l1=(i+j for i in l for j in l2 )
print(l1)#generator object it will print

l=['xy','lk','po']
l2=['aa','bb']
l1={i+j for i in l for j in l2 }
print(l1)

l=['xy','lk','po']
l2=['aa','bb']
l1=[i+j for i in l for j in l2 ]
print(l1)

l=[11,20,31,40,50]
l2=[20,30,40,50]
l1=[i+j for i in l for j in l2 ]
print(l1)

l=[11,20,31,40,50]
l1=[i for i in l if i%2==0]
print(l1)

l=[10,20,30,40,50]
l1=[i**2 for i in l]
print(l1)


l=[10,20,30,40,50]
l1=[i*2 for i in l]
print(l1)


l=[10,20,30,40,50]
l1=[i//2 for i in l]
print(l1)

l=input().split()
print(l)
l1=[int(i) for i in l]
print(l1)

l=input().split()
print(l)
l1=[]
for i in l:
    l1.append(int(i))
print(l1)


def checkpower(n):
    t=1
    while True:
        if 2**t==n and n<=2**t:
            return 1
        if 2**t>n:
            return 0
        t+=1
l=[10,4,6,8,45,16,32,10,64,128]
l1=[]
for i in l:
    l1.append(checkpower(i))
print(l1)


n1=7
n2=6
n3=n1 if n1>n2 else n2
while True:
    if n1%n3==0 and n2%n3==0:
        break
    n3-=1
print(n3)

n1=8
n2=10
n3=n1 if n1>n2 else n2
while True:
    if n3%n1==0 and n3%n2==0:
        break
    n3+=1
print(n3)

n=1000
t=0
p=0
while n>0:
    rem=n%10
    t+=rem*(2**p)
    n//=10
    p+=1
print(t)
    

n=8
t=''
while n>0:
    rem=n%2
    t+=str(rem)
    n//=2
print(int(t[::-1]))

l=[1,10,20,50,3,5,6]
l2=[10,20,30,40,50,60,70]
l3=[]
for i in range(len(l)):
    l3.append(l[i]+l2[-(i+1)])
print(l3)
    

l=[1,10,20,50,3,5,6]
L=l[0]
for i in range(len(l)):
    if L>l[i]:
        L=l[i]
print(L)

l=[1,10,20,50,3,5,6]
h=l[0]
for i in range(len(l)):
    if h<l[i]:
        h=l[i]
print(h)
    

def fib(n):
    f=0
    s=1
    if n==1 or n==2:
        return n-1
    for i in range(n-2):
        t=f+s
        f,s=s,t
    return t
n1=100
i=1
l=[]
while True:
    x=fib(i)
    if x>n1:
        break
    i+=1
    l.append(x)
print(l)
      

def fib(n):
    if n==1 or n==2:
        return n-1
    return fib(n-1)+fib(n-2)
a=fib(10)
print(a)

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
a=fact(5)
print(a)
    


def adddig(n):
    if n==0:
        return 0
    return n%10+adddig(n//10)
a=adddig(95654)
print(a)
    

def sample():
    print("inside sample block")
    return sample()
sample()

def fib(s):
    f=0
    s1=1
    if s==1 or s==2:
        return s-1
    for i in range(s-2):
        t=f+s1
        f,s1=s1,t
    return t
n=10
for i in range(1,n+1):
    print(fib(i),end=' ')

n=7
f=0
s=1
for i in range(n-2):
    t=f+s
    f,s=s,t
print(t)


def p(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
l=[10,13,20,31,41,19,17,16]
l1=[]
for i in l:
    if p(i):
        l1.append(i)
print(l1)

s="mvn87dm8360147hd87343"
s1=''
for i in s:
    if i>='0' and i<='9':
        s1+=i
for i in s1:
    if p(int(i)):
        print(i,end=' ')

def p(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
def emirp(m):
    rev=int(str(m)[::-1])
    if rev!=m:
        if p(m) and p(rev):
            return True
    return False
if emirp(19):
    print("emirp")
else:
    print("not emirp")


def p(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
s=10
e=100
l=[]
for i in range(s,e+1):
    if p(i):
        l.append(i)
print(l[-1]-l[0])
        

def p(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
if p(6):
    print('prime')
else:
    print("not prime")

def count(d):
    s=0
    d=d.upper()
    v='AEIOU'
    for i in d:
        if i in v:
            s+=1
    return s



x=count("engineering")
print(x)

s="engineering"
t=''
for i in s:
    if i not in t:
        t+=i
        print(f'{i}={s.count(i)}')
    
            

s="engineering"
s1={}
for i in s:
    s1[i]=s.count(i)
print(s1)
for k,v in s1.items():
    print(f'{k}={v}')
            


def count(s,s1):
    t=0
    for i in s:
        if i==s1:
            t+=1
    return t
def remove(n):
    t=''
    for i in n:
        if i not in t:
            t+=i
    return t
def rempveduplicate(m):
    x=remove(m)
    for i in x:
        print(f'{i}={m.count(i)}')
        
rempveduplicate("engineering")


def remove(n,m):
    t=0
    for i in n:
        if i==m:
            t+=1
    return t
x=remove("we are developers",'e')
print(x)
            


def remove(n,m):
    t=''
    return n.replace(m,t)
c=remove("we are developers",'e')
print(c)



def remove(n,m):
    t=''
    for i in n:
        if i not in m:
            t+=i
    return t
c=remove("we are developers",'e')
print(c)
    
           

def upper(s):
    s1=''
    for i in s:
        if (i>='A' and i<='Z' ):
            s1+=(chr(ord(i)+32))
        if (i>='a' and i<='z' ):
            s1+=(chr(ord(i)-32))
        else:
            s1+=i
    return s1
a=upper("BAda37dH77Q$BhJ")
print(a)


def upper(s):
    s1=''
    for i in s:
        if i>='A' and i<='Z':
            s1+=(chr(ord(i)+32))
        else:
            s1+=i
    return s1
a=upper("BADA37DH7230997Q@#$BHJ")
print(a)


n=101
c=n
while n>0:
    rem=n%10
    if rem==0:
        print(c,'duck number')
        break
    n//=10
else:
    print(c,'not a duck number')


s=1
e=500
for i in range(s,e+1):
    rev=int(str(i)[::-1])
    if i>1 and rev==i:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            print(i)
    

n=11
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,'not emirp')
            break
    else:
        rev=int(str(n)[::-1])
        if rev!=n:
            for i in range(2,rev//2+1):
                if rev%i==0:
                    print(n,'not emirp')
                    break
            else:
                print(n,'emirp')
        else:
            print(n,'not emirp')
else:
    print(n,'not emirp')

l=[]
for i in range(2,30):
    n=i
    for j in range(2,n//2+1):
        if n%2==0:
            break
    else:
        l.append(n)
        s=l[::2]
print(s)

n=17
b=True
for i in range(2,n//2+1):
    if n%i==0:
        b=False
        break
if b:
    print(n," prime")
else:
    print(n,"not prime")

n=145
c=n
t=0
while n>0:
    rem=n%10
    temp=1
    for i in range(1,rem+1):
        temp*=i
    t+=temp
    n//=10
if c==t:
    print("s")
else:
    print("not")


n=5
f=1
while n>0:
    f*=n
    n-=1
print(f)



n=5
temp=len(str(n))
last=(n**2)%(10**temp)
if n==last:
    print("auto mo")
else:
    print("not ")

t=0
count=len(str(n))
while n>0:
    t+=(n%10)**count
    count-=1
    n//=10
if c==t:
    print("armstrong number")
else:
    print("not arm strong number")
'''
