class a:
    x=10
class b(a):
    y=100
ob1=a()
ob2=b()
print(ob1.x)
print(a.x)
ob2.x=1000
print(ob1.x)
print(a.x)


print("child class")

print(ob2.x)
print(ob2.y)
print(b.x)
print(b.y)
