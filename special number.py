for i in range(10,50000):
    n=i
    temp=0
    while  i>0:
        rem=i%10
        fact=1
        for j in range(1,rem+1):
            fact*=j
        temp+=fact
        i//=10
    if n==temp:
        print(n)
