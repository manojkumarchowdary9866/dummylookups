class bank:
    Bname="icici"
    IFSC="icici0007"
    def __init__(self,name,acno,bal,pin):
        self.name=name
        self.acno =acno
        self.bal=bal
        self.pin=pin

    def withdraw(self,amt):
        if self.pin==bank.pin():
            if self.bal>=amt:
                print("withdraw successfully!!")
                self.bal-=amt
                print(f'available bal is:{self.bal}')
            else:
                print("insufficient bal")
        else:
            print("incorrect pin")
    @staticmethod
    def pin():
        password=int(input("password: "))
        return password
ob1=bank("manoj",85207410963321,1000000,1234)
ob2=bank("manu",85207410963278,1000000,12345)
ob1.withdraw(10000)
