#comprehension on list
'''l=input("enter n: ").split()
print(l)
l2=[]
for i in l:
    l2.append(int(i))
print(l2)

l2=[int(i)  for i in l   ]
     #expression       condition
print(l2)
l=[5,25, 36, 50 ]
l2=[1, 5, 7, 10]
#comprehension on set
l=["x","w","k","l"]
l2=["x","x","t","i"]
l3={i+j for i in l for j in l2}
print(l3)'''
#comprehension on dictonary
l=["dj","f2","rs","bn","rrr"]
l2=[10,20,40,50,65]
s={l[i]:l2[i] for i in range(len(l))}
print(s)
#ticketsprice
l1=['rs','bn','rrr']
l3=[140,50,150]
s1={l1[i]:l3[i] for i in range(len(l3))}
print(s1)
count=0
for i in s1:
    if s[i]!=s1[i]:
        count+=1
print(count)
