def checkpower(n):#2,4,8,16,32,64... 5<=8
    t=1
    while True:
        if 2**t==n and n<=2**t:#2**2<=4
            return 1
        elif 2**t>n:#2**3>5
            return 0
        t+=1

l=[2,5,4,46,8,25,16,23,32,56,64]#[1,0,1,0,1,0,1,0,1,0,1]
l2=[]
for i in l:
    l2.append(checkpower(i))
print(l2)
