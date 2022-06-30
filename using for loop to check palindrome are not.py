n=4554
c=""
s=str(n)
print(s)
print(type(s))
for i in s:
    c+=(i[::-1])
if n==int(c):
    print(c,'is palindrome')
else:
    print(c,'is not palindrome')
    
