def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

start=10
end=100
l=[]
for i in range(start,end+1):
    if prime(i):
        l.append(i)
print(l[-1]+l[0])
