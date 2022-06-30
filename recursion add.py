#add given digits  965365
def AddDig(s):
    if s==0:
        return 0
    return s%10+AddDig(s//10)


x=AddDig(965365)
print(f'add digits :{x}')
'''
5+AddDig(96536)
    (29)
  6+AddDig(9653)
      (23)
   3+AddDig(965)
      (20)
    5+AddDig(96)
       (15)
     6+AddDig(9)
        (9) 
      9+AddDig(0)
       (0)'''
