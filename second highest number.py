n = int(input())
arr = list(map(int, input().split()))
if  2<= n <=10 :
    d=[]
    for i in arr:
        if i not in d:
            d.append(i)
            d.sort()
print(d[-2])
