l=[2,4,5,66,7,1,4,56]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i])
        if l[i]>=l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
    
