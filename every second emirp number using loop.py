l=[]
for i in range(10,200):
    n=i
    if i>1:
        
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            rev=int(str(i)[::-1])
            if rev!=i:
                for m in range(2,rev//2+1):
                    if rev%m==0:
                        break
                else:
                    l.append(i)
                    s=l[1::2]
print(s)
