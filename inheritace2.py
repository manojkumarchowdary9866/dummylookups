class a:
    x=10
    def __init__(self):
        print("display class a")
class b(a):
    y=100

    def __init__(self):
        print("display class b")
ob1=a()
ob2=b()

