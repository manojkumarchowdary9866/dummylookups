#automorphic number
n=int(input("n: "))
g=len(str(n))
last=(n**2)%(10**g)
if n==last:
    print(n,"is automorphice number")
else:
    print(n,"is not  automorphice number")
    
