def checkpower(n):
    p=1
    while n>0:
        if 2**p==n and n<=2**p:
            return 1
        if 2**p>n:
            return 0
        p+=1
l=[10,210,4,23,24,16,32,250,64]
l2=[]
for i in l:
    l2.append(checkpower(i))
print(l2)
