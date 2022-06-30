#argtypes
'''1 postional arg
2 keyword arg
3 default arg
4 variable length arg
5 variable length and keyword arg'''
#default arg
def Fname(a,b="raj",c=0):
    print(f'a : {a}')
    print(f'b : {b}')
    print(f'c : {c}')
    print("*"*10)
    
#non default arg fallows default arg
#combination of positional and key word 
Fname(200,110,250)
Fname(200,110)
Fname(200)
