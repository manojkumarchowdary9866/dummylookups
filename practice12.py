from math import factorial
def fact(n):
    if n==0 or n==1:
        return 0
    return n*fact(n-1)
try:
    assert fact(5)==factorial(5),'assert error executed'
except AssertionError as msg:
    print(msg)
