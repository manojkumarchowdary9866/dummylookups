a=input()
i=int(input())
if ord(a)>=97:
    e=ord(a)-96+i
else:
    e=ord(a)-66+i
if e>26:
    e%=26
if ord(a)>=97:
    print(chr(e+96))
else:
    print(print(chr(e+65)))
