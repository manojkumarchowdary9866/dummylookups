class animal:
    place='zoo'
    def __init__(self,name):
        self.name=name
        print("obj created")
    @classmethod
    def modify(cls):
        print(cls.place)
    @classmethod
    def change(cls,newplace):
        cls.place=newplace
ob=animal('tiger')
animal.modify()
ob.modify()
print("after modifications")
ob.change('forest')
animal.modify()
ob.modify()

'''def out(arg):
    d={}
    def inn():
        if len(d)==0:
            d[arg]=arg()
        return d[arg]
    return inn

@out
class movie:
    def __init__(self):
        self.tickets=100
    def booking(self,n):
        if self.tickets>=n:
            print('tickets booked!!!')
            self.tickets-=n
            print(f'available tickets:{self.tickets}')
        else:
            print("tickets not avl")

def paytm():
    obj=movie()
    n=int(input("enter u ticktes: "))
    obj.booking(n)
paytm()
paytm()
paytm()
paytm()
paytm()
paytm()
paytm()
paytm()'''

    
        
    
