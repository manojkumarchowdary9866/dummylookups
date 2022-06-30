'''s="reach out to know much reach out to if u know much"
s1={}
s=s.upper()
v="AEIOU"
for i in s:
    if i in v:
        s1[i]=s.count(i)
print(s1)'''

'''
l=["manoj","raju","basav"]
s={i[0][0] for i in l}
print(s)'''

'''
d={i:i for i in range(1,11) if i%2==0 }
print(d)'''

'k={d[i],(True if i%2!=0 else False) for i in range(1,11)}'''
