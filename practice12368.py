'''import functools
l=[10,20,60,40,50]
m=functools.reduce(lambda x,y:x+y,l)
print(m)



x=10#30#90#130
y=20#60#40#50
x+y=30#90#130#180'''
from functools import reduce
l=[10,20,60,40,50]
m=reduce(lambda x,y:x-y,l)
print(m)

#x=10#-10#-70#-110
#y=20#60#40#50
#x-y=10#-70#-110-160

# from modulename import fuctionname
#vn=functonname(arg1,arg2)

#import modulename
#vn=modulename.functionname(arg1,arg2)

