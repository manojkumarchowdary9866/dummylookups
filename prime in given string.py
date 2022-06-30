def prime(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
s="mnxsngdq9we734ryifedjhci2t4864e88ye"
s1=''
for i in s:
    if i>='0' and i<='9':
        s1+=i
        
for i in s1:
    if prime(int(i)):
        print(i)
        
    
