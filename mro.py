class address():
    def __init__(self,street,locality,landmark):
        self.street=street
        self.locality=locality
        self.landmark=landmark
class emp():
    def __init__(self,name,iD,mno):
        self.name=name
        self.iD=iD
        self.mno=mno
        self.add=address('munekallu','bangalore',"temple")
    def dsp(self,):
        print(f'name    :{self.name}')
        print(f'id      :{self.iD}')
        print(f'mno     :{self.mno}')
        print(f'street  :{self.add.street}')
        print(f'locality:{self.add.locality}')
        print(f'landmark:{self.add.landmark}')



e=emp('manoj',9887,9866847308)
e.dsp()

print('*'*20)

e1=emp('raju',85,8555454444)
e1.dsp()
