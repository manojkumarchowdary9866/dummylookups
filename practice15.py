'''l=[10,20,60,2,3,5,80,63,5]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
        
            l[i],l[j]=l[j],l[i]
print(l)

l=[1,2,3,2,2,3,5,6,2,1,3,4]
c=0
while c<len(l):
    c2=c+1
    while c2<len(l):
        if l[c]==l[c2]:
            l.pop(c2)
        else:
            c2+=1
    c+=1
print(l)                
l=[1,2,3,2,2,3,5,6,2,1,3,4]
l=list(dict.fromkeys(l))
print(l)
'''
