class bank():
    Bname="hdfc"
    IFSC="HDFC00007"

    def __init__(self,Name,Mno,Bal):
         self.name=Name
         self.mno=Mno
         self.bal=Bal

    def details(self):
        print(f'name= {self.name}')
        print(f'bal =  {self.bal}')
        print(f'mno = {self.mno}')
    def deposit(self,amt):
        self.bal+=amt

        print("deposit successfully")
        print(f"{self.name} available bal is {self.bal}")
    def withdraw(self,amt):
        if self.bal>=amt:
            self.bal-=amt
            print("withdraw success fully")
            print(f"{self.name} available is {self.bal}")
        else:
            print("insuficeint bal")


ob1=bank("manoj",9866847308,1000)
ob2=bank("raj",9638520741,50000)
ob1.deposit(10000)
ob2.deposit(20000)
print("*"*20)
ob1.withdraw(5000)
ob2.withdraw(8000)
