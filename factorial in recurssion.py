#factorial of recurssion  5=5*4*3*2*1
def fact(k):
    if k==0 or k==1:
        return 1
    return k*fact(k-1)

a=fact(5)
print(f'factorial of :{a}')

'''
 5*fact(4)
 4*fact(3)
 3*fact(2)
 2*fact(1)'''
 
