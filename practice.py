class b_v1():
    def __init__(self,name,mno):
        self.name=name
        self.mno=mno
    def disp(self):
        print(f'name:{self.name}')
        print(f'mno:{self.mno}')
class b_v2(b_v1):
    def __init__(self,name,mno,adno):
        super().__init__(name,mno)
        self.adno=adno
    def disp(self):
        super().disp()
        print(f'adno:{self.adno}')
class b_v3(b_v2):
    def __init__(self,name,mno,adno,gmail):
        super().__init__(name,mno,adno)
        self.gmail=gmail
    def disp(self):
        super().disp()
        print(f'gmail:{self.gmail}')
ob=b_v3("manoj",968574748,228523642834,"gade.manojkc@gmail.com")
ob.disp()
