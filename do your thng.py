def j(s):
    x=str(s)
    for i in range(1,len(x)):
        r=int("".join(x[1::-1]))
        l=int("".join(x[-2::1]))
    print(r,l)
    print(r+l)
j(4325)
