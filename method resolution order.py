class a:
    pass
class b:
    pass
class c(b,a):
    pass
print(c.__mro__)
