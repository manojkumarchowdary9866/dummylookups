class bank():
    bname='jagan'
    IFSC='jagan420'
    def __init__(self,name,mno,bal):
        self.name=name
        self.mno=mno
        self.bal=bal
    def disp(self):
        print(f'name:{self.name}')
        print(f'mno :{self.mno}')
        print(f'bal :{self.bal}')
        print('*'*20)
ob1=bank('manu',963852852,10)
ob2=bank('srk',852456556,10000)
ob1.disp()
ob2.disp()

    
