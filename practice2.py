def movie(arg):
    s={}
    def inner():
        if len(s)==0:
            s[arg]=arg()
        return s[arg]
    return inner
@movie
class cenima():
    def __init__(self):
        self.tickets=100
    def booking(self,n):
        if self.tickets>=n:
            print("ticket is booked")
            self.tickets-=n
        else:
            print("ticket unavailable")
def bookmyshow():
    ob1=cenima()
    n=int(input("enter no tickets: "))
    ob1.booking(n)


bookmyshow()
bookmyshow()
bookmyshow()
bookmyshow()
bookmyshow()
bookmyshow()
