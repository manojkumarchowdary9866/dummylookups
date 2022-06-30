class student():
    college='sri vaani degree clg'
    nob=2
ob=student()
ob1=student()
def details(obj,sname,mno,blood,rno):
    obj.sname=sname
    obj.mno=mno
    obj.blood=blood
    obj.rno=rno
details(ob,'bhargavi',9638520741,'o+',123)
details(ob1,'sravani',9638520743,'o-',124)
    
print(ob.sname,ob.mno,ob.blood,ob.rno)
print(ob1.sname,ob1.mno,ob1.blood,ob1.rno)
'''print(ob.college,ob.nob)
print(ob1.college,ob1.nob)
print(student.college,student.nob)
print("*"*20)
ob.college='svit college'
print(ob.college,ob.nob)
print(ob1.college,ob1.nob)
print(student.college,student.nob)'''

   
   
