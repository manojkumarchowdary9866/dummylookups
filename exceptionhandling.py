l=[10,100,1000,60,80]
a=3
try:
    for i in l:
        print(i//a)
        a-=1
except ZeroDivisionError as msg:
    print(msg)
except:
    print("exception block is excuted")
