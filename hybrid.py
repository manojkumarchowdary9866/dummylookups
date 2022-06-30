class parent:
    def __init__(self,name,mno):
        self.name=name
        self.mno=mno
    def display(self):
        print(f'name:{self.name}')
        print(f'mno:{self.mno}')
class child1(parent):
    def __init__(self,name,mno,adno):
        parent.__init__(self,name,mno)
        self.adno=adno
    def display(self):
        parent.display(self)
        print(f'adno: {self.adno}')
class child2(parent):
    def __init__(self,name,mno,pan):
        parent.__init__(self,name,mno)
        self.pan=pan
    def display(self):
        parent.display(self)
        print(f'pan: {self.pan}')
class gradchild(child1,child2):
    def __init__(self,name,mno,adno,pan,voterid):
        child1.__init__(self,name,mno,adno)
        child2.__init__(self,name,mno,pan)
        self.voterid=voterid
    def display(self):
        super().display()
        super().display()
        print(f'voterid: {self.voterid}')
ob1=gradchild("manoj",9866847308,228523642838,"abh6924k",45684)
ob1.display()
    
        
