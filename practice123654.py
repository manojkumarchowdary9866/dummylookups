'''n = int(input("n: "))
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and ((2<=n >=5) or (6 <= n >= 20)):
    print(" Weird")
else:
    print("NOt Weird")'''
'''l=[1,2,3,4,5,6,7,8,9]
d=dict.fromkeys(l,0)
print(d)
l1=[2, 3, 7, 12, 14, 9, 24, 27, 82, 81, 95]
for i in l:
    for j in l1:
        if j%i==0:
            d[i]=d[i]+1
print(d)'''
'''n=5
star=1
space=n-1
for i in range(n):
    temp=1
    for j in range(space):
        print(" ",end=" ")
    for k in range(star):
        print(temp+i,end=" ")
        if k<star//2:
            temp+=1
        else:
            temp-=1
    print()
    star+=2
    space-=1'''
'''x='H'
y=23
z=ord(x)+y-65
print(chr((z%26)+65))
n=9865413
c=0
while n>0:
    if (n%10)%2==0:
        c+=1
    n//=10
print(c)
s="manoj"
s1=""
for i in range(len(s)):
    s1+=s[-(i+1)]
print(s1)'''
'''def outer(arg):
    print(f'arg: {arg}')
    d={}
    def inner():
        i
        x=arg()#object creation
        return x
    return inner#innerfunction call

@outer
class a:
    def __init__(self):
        print("object created")

obj=a()
print("obj:{obj}")'''


'''def is_leap(year):
    leap = False

    if (year%100!=0 or year%4== 0) and year % 400 == 0:
        return True
    return leap


year = int(input())
print(is_leap(year))
'''
n=int(input())
star=1
for i in range(n):
    temp=1
    for j in range(star):
        print(temp,end="")
        if j<star//2:
            temp+=1
        else:
            temp-=1
    print()
    star+=2

