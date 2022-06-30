d={1:100,2:200,3:300,4:400}
print("get method")
print(d.get(2,1000))#200
print(d.get(5,1000))#1000
print(d.get(6))#None
print(d)
print("*"*30)
print("set default")
print(d.setdefault(3,2000))#300
print(d.setdefault(5,2000))#2000
print(d.setdefault(6))#None
print(d)

