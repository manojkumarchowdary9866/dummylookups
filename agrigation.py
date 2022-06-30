class adress():
    def __init__(self,street,locality,city):
        self.street=street
        self.locality=locality
        self.city=city
class employee():
    def __init__(self,name,Id,add):
        self.name=name
        self.Id=Id
        self.addr=add
    def dsp(self):
        print(self.name)
        print(self.Id)
        print(self.addr.street)
        print(self.addr.locality)
        print(self.addr.city)

add=adress("marthahalli","munekallu","bengalore")
ob=employee("manoj",56556,add)
ob.dsp()
print("*"*20)
add1=adress("marthahalli","munekallu","bengalore")
ob1=employee("manojkc",556,add1)
ob1.dsp()
