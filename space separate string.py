n=input().split()
print(n)
for i in range(0,len(n),1):
    if i%2==0:
        print(n[1+i-1]+n[i+1],end=" ")
