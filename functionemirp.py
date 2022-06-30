def prime(s):
    if s==1:
        return False
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
def emirp(s):
    rev=int(str(s)[::-1])
    if prime(s) and prime(rev) and rev!=s:
        return True
    return False

if emirp(17):
    print("emirp")
else:
    print("not emirp")
    
