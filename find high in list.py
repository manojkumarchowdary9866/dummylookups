#find given list in highest value
l=[1,2,10,5,92,10,85,36,63]#92
L=l[0]
for i in range(len(l)):
    if L>l[i]:
        L=l[i]
print(L)
