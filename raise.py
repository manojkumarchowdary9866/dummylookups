class error(Exception):
    pass
class error1(error):
    pass
class error2(error):
    pass
class error3(error):
    pass
try:
    raise error3
except error1:
    print("inside error1")
except error2:
    print("inside error2")
except error3:
    print("inside error3")
