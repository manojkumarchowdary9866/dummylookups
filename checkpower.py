def checkpower(n):
    temp=1
    while n>0:#True
        if 2**temp==n and n<=2**temp:
            return 1
        elif 2**temp>n:
            return 0
        temp+=1

l=[11,12,8,25,16,24,36,56,64,123,128]
l1=[]
for i in l:
    l1.append(checkpower(i))
print(l1)
