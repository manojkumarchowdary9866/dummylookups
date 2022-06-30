class adress():
    def __init__(self,street,locality,city):
        self.street=street
        self.locality=locality
        self.city=city
class employee():
    def __init__(self,name,Id):
        self.name=name
        self.Id=Id
        self.addr=adress("marthahalli","munekallu","bengalore")
    def dsp(self):
        print(self.name)
        print(self.Id)
        print(self.addr.street)
        print(self.addr.locality)
        print(self.addr.city)

ob=employee("manoj",56556)
ob.dsp()
print("*"*20)
ob1=employee("manojkc",556)
ob1.dsp()
