class parent:
    x=10
    y=20
class c(parent):
    z=30
ob1=parent()
ob=c()
print("modify with child class  object name")
ob.x=100
print('using parent cls name')
print("x:",parent.x)#10
print(parent.y)#20
#print(parent.z)#error
print('using parent cls object name')
print("x:",ob1.x)#10
print(ob1.y)#20
#print(ob1.z)#error
print('using child cls name')
print("x:",c.x)#10
print(c.y)#20
print(c.z)#30
print('using child cls  object name')
print("x:",ob.x)#100
print(ob.y)#20
print(ob.z)#30
