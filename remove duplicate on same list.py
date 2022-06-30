l=[1,1,2,3,4,3,2,1]
count=0
while count<len(l):
    count2=count+1
    while count2<len(l):
        if l[count]==l[count2]:
             l.pop(count2)
        else:
            count2+=1
    count+=1
print(l)
