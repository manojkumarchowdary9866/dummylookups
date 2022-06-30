z=int(False)
o=int(True)
h=int(f'{o}{z}{z}')
print(h)
def an(g):
    if g<=h:
        print(g,end=' ')
        an(g+o)
an(o)


'''
while z<=h:
    if z!=int(False):
        print(z,end=' ')
    z+=o


for i in range(o,h+o):
    print(i,end=' ')

'''
