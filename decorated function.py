def outer(arg):
    print("enetering outer functon")
    print(f'arg:{arg}')
    def inner():
        print("entering inner function")
        arg()
        print("exiting inner functon")
    print("exiting outer inner function")
    return inner
@outer
def sample():
    print("sample function executed")
print(f"sample:{sample}")
sample()
