class bank:
    Bname='union bank'
    IFSC='UNION00007'
    NOB=100
    def __init__(self,Name,ACNO,adno,mno):
        self.Name=Name
        self.ACNO=ACNO
        self.adno=adno
        self.mno=mno
    

ob1=bank("charan",97010110075898,228569694568,9866847308)
ob2=bank("ss",97010100075865,2365985552122,7075866213)
ob3=bank("ram",97010100075869,2365985552124,7075866216)
del ob1.ACNO
#print(ob1.Name,ob1.ACNO,ob1.adno,ob1.mno)
print(ob2.Name,ob2.ACNO,ob2.adno,ob2.mno)
print(ob3.Name,ob3.ACNO,ob3.adno,ob3.mno)


