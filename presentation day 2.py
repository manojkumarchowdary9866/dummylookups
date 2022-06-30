def prime(s):
    s1=int(str(s)[::-1])
    if s>1 and s!=s1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
        
    return True
        
        
    
l=[]
for i in range(10,1000):
    if prime(i):
        l.append(i)
print(l)
    
        
        
