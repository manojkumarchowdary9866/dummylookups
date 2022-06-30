#types inheritance 5
'''1 single
2 hireiarchale
3 multiple
4 multi level
5 hybride'''

class p:
    def dsp(self):
        print('dhoni')
class p1:
    def dsp(self):
        print('sakshi')
class c(p1,p):
    def dsp(self):
        p.dsp(self)
        p1.dsp(self)
        print("jeeva")
ob=c()
ob.dsp()

