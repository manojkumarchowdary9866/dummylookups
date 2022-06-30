'''
#duck typing
class pycharm:
    def execute(self):
        print("comiling")
        print("running")
class myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("comiling")
        print("running")
class laptop:
    def code(self,ide):
        ide.execute() 
ide=myeditor()
lap=laptop()
lap.code(ide)


#inner class
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
        def show(self):
            print(self.brand,self.cpu)
        
ob=student('manoj',5)
ob.show()
lap1=student.laptop()
'''
