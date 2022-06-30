l=[10,20,30,40]
l1=[1,2,3,4]
l2=[]
for i in range(len(l)):
    l2.append(l[i]+l1[-(i+1)])
print(l2)
