def out(arg):
    def inner():
        arg(4,5)
    return inner
@out
def sam(a,b):
    print(a+b)

sam()
