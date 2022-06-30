class x:
    pass
class y:
    pass
class b(x,y):
    pass
class c(y,x):
    pass
class d(b,c):
    pass
print(d.__mro__)#TypeError: Cannot create a consistent method resolution
#order (MRO) for bases x, y
'''
class x:
    pass
class y:
    pass
class b(x,y):
    pass
class c(x,y):
    pass
class d(b,c):
    pass
print(d.__mro__)#d,b,c,x,y,object in tuple data type




class x:
    pass
class y:
    pass
class b(x,y):
    pass
class c(y):
    pass
class d(b,c):
    pass
print(d.__mro__)#d,b,x,c,y,object in tuple data type


class a:
    pass
class b:
    pass
class c(a):
    pass
class d(b):
    pass
class e(d,c):
    pass
print(e.__mro__)#e,d,b,c,a,object in tuple data type



class a:
    pass
class b(a):
    pass
class c(a):
    pass
class d(c,b):
    pass
print(d.__mro__)#d,c,b,a,object in tuple data type




class a:
    pass
class b(a):
    pass
class c(b):
    pass
print(c.__mro__)#c,b,a,object tuple data

class a:
    pass
class b:
    pass
class c(a,b):
    pass
class d(b,a):
    pass
print(c.mro())#c,a,b,object in list data type
print(d.mro())#d,b,a,object'''
