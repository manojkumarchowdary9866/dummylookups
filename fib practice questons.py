'''def fib(l):
    if l==1 or l==2:
        return l-1
    return fib(l-1)+fib(l-2)


n=26
d={}
s='MNX'
g=0
for i in range(1,n+1):
    d[chr((i)+64)]=fib(i+2)
print(d)
for i in s:
    if i in d:
        g+=d[i]
print(f'MNX: {g}')


#sum of odd index postions in vowels
s='manoj'
v='aeiou'
t=0
for i in range(len(s)):
    if s[i] in v:
        if i%2!=0:
            t+=i
print(t) '''

#sum of even index postions consonant
s='manoj123'
v='aeiou'
t=0
for i in range(len(s)):
    if s[i].isalpha():
        if s[i] not in v:
            if i%2==0:
                t+=i
print(t)
'''

d={'A':1,'B':2}
for i in range(67,91):
    d[chr(i)]=d[chr(i-1)]+d[chr(i-2)]
print(d)














