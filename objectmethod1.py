class bank():
    bname='f2'
    IFSC='f20001'

    def __init__(self,name,accno,mno,bal):
        self.name=name
        self.accno=accno
        self.mno=mno
        self.bal=bal
    def deposit(self,amt):
        self.bal+=amt
        print('deposit successfully')
        print(f'{self.name} available bal is {self.bal}')
    def withdraw(self,amt):
        if self.bal>=amt:
            self.bal-=amt
            print('withdraw successfully!!!')
            print(f'{self.name} available bal is {self.bal}')
        else:
            print("insufficient bal")

ob1=bank('raj',97048636598715,705866213,10000)
ob2=bank('boss',97048636598756,705866216,999999)
ob3=bank('balayya',97546698741326,9866841265,953265)
#ob1.withdraw(100000)
ob1.deposit(1000)
