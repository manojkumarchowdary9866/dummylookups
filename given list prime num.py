def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
l=[11,12,14,17,19,15,16,23]
l2=[]
for i in l:
    if prime(i):
        l2.append(i)
print(l2)
