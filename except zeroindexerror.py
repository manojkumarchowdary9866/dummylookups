l=[10,20,30]
a=1
try:
    for i in range(len(l)):
        print(l[a]//a)
        a-=1
except ZeroDivisionError as m:
    print(m)


