l=[10,20,30]
a=2
try:
    for i in l:
        print(i//a)
        a-=1
except:
    print('inside except block')
