from functools import reduce as r
l=[10,20,30,50,80,90]
x=r(lambda x,y:x-y,l)
print(x)

'''
#functools
from functools import reduce as r
l=[10,20,30,50,80,90]
x=r(lambda x,y:x-y,l)
print(x)

l=input("l: ").split()
m=list(map(int,l))
print(l)
print(m)


#filter
l=[10,20,30,5,56]
m=list(filter(lambda x:x%10==0,l))
print(m)#[10,20,30]

l=[10,20,30,5,56]
m=list(map(lambda x:x*10,(filter(lambda x:x%10==0,l))))
print(m)#[100,200,300]


#map function
def mul(n):
    return n*10
l=[10,20,30]
m=list(map(mul,l))
print(m)

l=[10,20,30]
m=list(map(lambda x:x*10,l))
print(m)#[100,200,300]

l=[10,20,30,5,56]
m=list(map(lambda x:x%10==0,l))
print(m)#[True, True, True, False, False]


#lambda/annonymous functions
add=lambda a,b,c:a+b+c
x=add(110,30,50)
print(x)

#comprehension
l=input("l: ").split()
l3=[int(i) for i in l]
print(l3)

l=input("l: ").split()
l3=[int(i)*2 for i in l]
print(l3)

l=input("l: ").split()
l3=[int(i)//2 for i in l]
print(l3)

l=[10, 20, 25, 35, 26, 28, 10]
l3=[i for i in l if i%5==0]
print(l3)

l=[10, 20, 25, 35, 26, 28, 10]
l2=[10, 20]
l3=[i+j for i in l for j in l2 ]
print(l3)

l=['mk','dd','ddde','fed']
l2=['dfgv','df','edf']
l3=[i+j for i in l for j in l2 ]
print(l3)

l=['mk','dd','ddde','fed']
l2=['dfgv','df','edf']
l3=(i+j for i in l for j in l2 )
print(l3)#generator object

l=[1,2,3]
l2=['dfgv','df','edf']
l3={l[i]:l2[i] for i in range(len(l)) }
print(l3)

#2
l1=[1,3]
l4=['dfgv','edf']
l5={l1[i]:l4[i] for i in range(len(l1)) }
print(l5)
count=0
for i in l5:
    if l3[i]==l5[i]:
        count+=1
print(count)

#set comprehension only same data type
l=['1','2','3']
l2=['dfgv','df','edf']
l3={i+j for i in l for j in l2 }
print(l3)

l=[1,2,3,4]
l2=[10,20,30]
l3={i+j for i in l for j in l2 }
print(l3)


l=input("l: ").split()
l3=[]
for i in l:
    l3.append(int(i))
print(l3)

#checkpower
def checkpower(s):
    temp=1
    while True:
        if 2**temp==s and s>=2**temp:
            return 1
        elif 2**temp>s:
            return 0
        temp+=1
l=[2,4,6,8,3,12,16,48,32,64,56,128]
l2=[]
for i in l:
    l2.append(checkpower(i))
print(l2)

#hcf
n=8
n2=10
n3=n1 if n>n2 else n2
while True:
    if n%n3==0 and n2%n3==0:
        break
    n3-=1
print(n3)

#lcm
n=8
n2=10
n3=n1 if n>n2 else n2
while True:
    if n3%n==0 and n3%n2==0:
        break
    n3+=1
print(n3)


#binary to number
n=111000
t=0
p=0
while n>0:
    r=n%10
    t+=r*(2**p)
    p+=1
    n//=10
print(t)


#number to binary
n=56
t=''
while n>0:
    r=n%2
    t+=str(r)
    n//=2
print(int(t[::-1]))

#add corresponding index postion
l=[10,20,30,50,10,30,60,8,6,9]
l1=[10,20,30,50,10,30,60,8,6,9]
l2=[]
for i in range(len(l)):
    l2.append(l[i]+l1[i])      
print(l2)

l=[10,20,30,50,10,30,60,8,6,9]
l1=[10,20,30,50,10,30,60,8,6,9]
l2=[]
for i in range(len(l)):
    l2.append(l[i]+l1[-(i+1)])      
print(l2)


#highest and lowest
l=[10,20,30,50,10,30,60,8,6,9]
h=l[0]
for i in range(len(l)):
    if h>l[i]:#lowest #h<l[i]# highest
        h=l[i]
        
print(h)


s='abc'
s1='def'
s3=''
for i in range(len(s)):
    s3=s[i]+s1[i]
    print(s3,end='')
#op>adbecf

#special charcter extraction
def fib(n):
    s=''
    n=n.upper()
    for i in n:
        if not((i>='A' and i<='Z') or(i>='0' and i<='9')):
            s+=i
    return s
x=fib('@#$%^&dfghj')
print(x)


#check given number is fibnoccial series or not
def fib(n):
    if n==1 or n==2:
        return n-1
    return fib(n-1)+fib(n-2)
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

#recurrssion fib
def fib(n):
    if n==1 or n==2:
        return n-1
    return fib(n-1)+fib(n-2)
x=fib(5)
print(x)

#recurrssion factorial
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
x=fact(5)
print(x)


#recurrssion adddigits
def addDig(n):
    if n==0:
        return 0
    return n%10+addDig(n//10)
x=addDig(963852741)
print(x)





#fibnocciseries first 10 number
def fib(s):
    f=0
    se=1
    if s==1 or s==2:
        return s-1
    for i in range(s-2):
        t=f+se
        f,se=se,t
    return t
l=[]
for i in range(1,11):
    l.append(fib(i))
print(l)



#fibnocci series
n=7
f=0
s=1
for i in range(n-2):
    t=f+s
    f,s=s,t
print(t)

#given string print prime numbers
def prime(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
l='j856d8839745702384566xchjk'
l1=''
for i in l:
    if i>='0' and i<='9':
        l1+=i
for i in l1:
    if prime(int(i)):
        print(i)


#list inside print emirpnumbers
def prime(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
def emirp(s):
    rev=int(str(s)[::-1])
    if prime(s) and prime(rev):
        return True
    return False
l=[10,12,13,17,18,19,23,16,37]
l1=[]
for i in l:
    if emirp(i):
        l1.append(i)
print(l1)



#emirp number
def prime(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
def emirp(s):
    rev=int(str(s)[::-1])
    if prime(s) and prime(rev):
        return True
    return False

if emirp(19):
    print("emirp")
else:
    print("not emirp")



#df bw lowest and highest prime
def prime(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True

n=100
l=[]
for i in range(1,n+1):
    if prime(i):
        l.append(i)
print(l[-1]-l[0])


#prime number
def prime(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True

if prime(136):
    print('prime number')
else:
    print("not prime")

#count vowels
def cv(s):
    s1=0
    s=s.upper()
    v='AEIOU'
    for i in s:
        if i in v:
            s1+=1
    return s1
x=cv("we are devops and usually freeking")
print(x)  

#extract numbers
def digits(s):
    s1=''
    for i in s:
        if i>='0' and i<='9':
            s1+=i
    return s1
x=digits("mbff797rfh7w3rtgh7283try8q7346")
print(x)    



#count digits
def digitcount(s):
    s1=0
    for i in s:
        if i>='0' and i<='9':
            s1+=1
    return s1
x=digitcount("mbff797rfh7w3rtgh7283try8q7346")
print(x)    


#without using dictonary
s='engineering'
d=''
for i in s:
    if i not in d:
        d+=i
        print(f'{i}={s.count(i)}')


#using dictonary
s='engineering'
d={}
for i in s:
    d[i]=s.count(i)
print(d)
for k,v in d.items():
    print(f'{k}={v}')

#counteachchr
def count(n,m):
    t=0
    for i in n:
        if i==m:
            t+=1

    return t

def remove(n):
    t=''
    for i in n:
        if i not in t:
            t+=i
    return t
def counteach(s):
    s1=remove(s)
    for i in s1:
        print(f'{i}={s.count(i)}')
counteach('engineering')


#removeduplicates
def remove(n):
    t=''
    for i in n:
        if i not in t:
            t+=i
    return t

x=remove("tenetnetten")
print(x)



#count duplicates
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
    for i in n:
        if i not in m:
            t+=i
    return t

x=remove("we are developers",'e')
print(x)



def remove(n,m):
    t=''
    return n.replace(m,t)

x=remove("we are developers",'e')
print(x)'''
