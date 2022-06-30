l=[1,2,3,4,5,6,7,8,9]
d=dict.fromkeys(l,0)
print(d)
l1=[2, 3, 7, 12, 14, 9, 24, 27, 82, 81, 95]
for i in l:
    for j in l1:
        if j%i==0:
            d[i]=d[i]+1
print(d)
