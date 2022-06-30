#lambda functions #annonymous
'''vn=lambda a,b,c:a*b*c
x1=vn(10,20,30)
print(x1)
fn=lambda Fn,Ln:f'{Fn} {Ln}'
x=fn("abhay","ram")
print(x)

def mul(n):
    return n*10

l=[10,2,30,4]
m=list(map(mul,l))
print(m)
#vn=list(map(arg1,arg2))
#arg1=functionname
#arg2=collection datatype
 #filter
def even(n):
    return n%2==0
l=[1,3,15,14,12,16,3]
x=list(filter(even,l))
print(x)

def checkpower(n):
    p=1
    while True:
        if 3**p==n and n<=3**p:#3**1==3
            return 1
        elif 3**p>n:
            return 0
        p+=1


l=[12,15,3,4,9,15,27,15,64,81]#[0,0,1,0,1,0,1,0,1]
l2=[]
for i in l:
    l2.append(checkpower(i))
print(l2)
l=input("enter your numbers: ").split()
print(l)
x=list(map(lambda y:int(y),l))
print(x)
l2=[]
for i in l:
    l2.append(int(i))
print(l2)'''
#comprehension on dictonary
d=["csk","srh","mi","rcb"]
d1=[14,10,10,6]
#d3=dict(zip(d,d1))
d3={d[i]:d1[i]  for i in range(len(d1))}    
print(d3)
d4=["csk","srh","mi"]
d5=[16,12,10]
dd={d4[i]:d5[i]    for i in range(len(d5))}
print(dd)
count=0
for i in dd:
    if d3[i]!=dd[i]:
        count+=1
print(count)






























    
    
    










    
