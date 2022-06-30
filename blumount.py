n=7
s='<>'
s1='><'
star=1
for i in range(n):
    for j in range(star):
        if i%2==0 and j%2==0:
            print(s,end='')
        elif i%2!=0 and j%2!=0:
            print(s,end='')
        else:
            print(s1,end='')
    print()
    star+=1
