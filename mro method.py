class a:
    def sam(self):
        print("krk heroine")
class b(a):
    def sam(self):
        a.sam(self)
        print("manam heroine")
        super().sam()
ob=b()
ob.sam()
        
