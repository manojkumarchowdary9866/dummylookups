n=5
star=1
for i in range(n):
    temp=1
    for  j in range(star):
        print(temp,end=" ")
        if j<star//2:
            temp+=1
        else:
            temp-=1
    print()
    star+=2
    
