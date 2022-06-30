try:
    a=int(input("a: "))
    b=int(input("b: "))
    if b==0:
        try:
            b=int(input("b>0: "))
            print(a/b)
        except:
            print("except occured")
except:
    print("except occured")

else:
    print(a/b)

finally:
    print("inside finally block")
    
    
