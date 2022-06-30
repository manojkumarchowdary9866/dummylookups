def outer(arg):
    s={}
    def inner():
        if len(s)==0:
            s[arg]=arg()#decorated function call
        return s[arg]
    return inner

@outer
class a():
    def __init__(self):
        self.tickets=100
    def booking(self,n):
        if self.tickets>=n:
            print("ticket is booked!!")
            self.tickets-=n
        else:
            print("tickets unavailable")
def bookmyshow():
    ob1=a()
    n=int(input("enter number of tickets: "))
    ob1.booking(n)
        
bookmyshow()
bookmyshow()
