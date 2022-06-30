def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
s="anc7d4sj82m96sh3j1a17s5"
s1=""
for i in s:
    if i>="0" and i<="9":
        s1+=i
print(s1)
for i in s1:
    if prime(int(i)):
        print(i,'prime')
