s=[1,10,23,7,10,3,3,90]
s1=[]
for i in s:
    if s.count(i)!=1:
        s1.append(i)
        
print(list(set(s1)))
