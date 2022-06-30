class bank:
    name="sbi bank"
    IFSC='SBI0007'
    nob=50
    def __init__(self,name,acno,mno,bal,pin):
        self.name=name
        self.acno=acno
        self.mno=mno
        self.bal=bal
        self.pin=pin
    def withdraw(self,amt):
      if self.pin==bank.PIN(): 
            if self.bal>=amt:
                self.bal-=amt
                print("withdraw successfully")
                print(f' {self.name} availa bal is{self.bal}')
            else:
                print("insuficient bal")
      else:
         print("incorrect pin")
    
    @staticmethod
    def PIN():
        p=int(input("enter ur password: "))
        return p

ob=bank('manu',97084569852312,9874563216,10000,9866)
ob2=bank('rosi',97084569852314,9874563217,90000,7075)
#ob.withdraw(9000)
ob2.withdraw(9000)
