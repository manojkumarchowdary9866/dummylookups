class p():
    def disp(self):
        print("dance")
class p2():
    def disp(self):
        print("cooking")
class p3():
    def disp(self):
        print("working")
class cc(p,p2,p3):
    def disp(self):
        p.disp(self)
        p2.disp(self)
        p3.disp(self)
        print("acting")
ob=cc()
ob.disp()
        
