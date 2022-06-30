l=[4,1,5,3,9]
h=l[0]
k=[]
for i in l:
    if h<i:
        h=i
        k.append(h)
x=set(k)
print(list(x))
    
        

