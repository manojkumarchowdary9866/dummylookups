def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def emirp(n):
    rev=int(str(n)[::-1])
    if n!=rev:
        if prime(n) and prime(rev):
            return True
    return False
y=17
if emirp(y):
    print("emirp number")
else:
    print("not emirp number")
