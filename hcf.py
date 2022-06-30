n1=12
n2=4
res=n1  if n1>n2 else n2
while not(n1%res==0 and n2%res==0):
    res-=1
    
print(res)
