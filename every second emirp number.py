def prime(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
def emirp(s):
    rev=int(str(s)[::-1])
    if s!=rev:
        if prime(s) and prime(rev) :
            return True
    return False
l=[]
for k in range(10,100):
    if emirp(k):
        l.append(k)
        m=l[1::2]
print(l)
print(m)
