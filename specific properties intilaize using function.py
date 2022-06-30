class student():
    Cname="pvkk college"
    NOB=50


ob1=student()
ob2=student()
def details(obj,Name,Mno,Adno):
    obj.name=Name
    obj.mno=Mno
    obj.adno=Adno

details(ob1,"manoj",9638527410,6541239877410)
details(ob2,"mad",9638527420,6541239877420)
'''print(ob1.__dict__)
print(ob2.__dict__)'''
print(ob1.name,ob1.mno,ob1.adno)
print(ob2.name,ob2.mno,ob2.adno)
