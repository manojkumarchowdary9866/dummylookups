n1=8
n2=4
res=n1  if n1<n2 else n2
while True:
    if res%n1==0 and res%n2==0:
        break
    res+=1
    
print(res)
