'''s='aaabbbccaabb'
c=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        print(s[i],c)
        c=1




'''
l='i32 am good python programming language'
l1=l.split()
l2=sorted(l1,key=len, reverse=True)
s1=''
for i in l2:
    s1=s1+i+' '
print(s1)
