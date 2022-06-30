class prime(Exception):
    def __str__(self):
        return "magic method executed"
try:
    n=int(input("n: "))
    for i in range(2,n//2+1):
        if n%i==0:
            raise prime(n,"not prime")
except prime as msg:
    print(msg)
