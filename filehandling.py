
'''
#reading pickle data into file by using load:
with open('manbinary.txt','rb') as file:
    import pickle
    pd=pickle.load(file)
    print(pd)
output:
{'name': 'sorry seshu', 'age': 24}

#reading pickle data into file by using loads:
with open('manbinary.txt','rb') as file:
    import pickle
    bd=file.read()
    print(bd)
    pd=pickle.loads(bd)
    print(pd)
#output
b'\x80\x04\x95"\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x0bsorry seshu\x94\x8c\x03age\x94K\x18u.'
{'name': 'sorry seshu', 'age': 24}
    
#writing pickle data into file by using dump:
with open('manbinary1.txt','wb') as file:
    import pickle
    d={'name':'sorry seshu','age':24}
    pickle.dump(d,file)

#writing pickle data into file by using dumps:
with open('manbinary.txt','wb') as file:
    import pickle
    d={'name':'sorry seshu','age':24}
    print(d)
    bd=pickle.dumps(d)
    print(bd)
    print(type(bd))
    file.write(bd)
#output
{'name': 'sorry seshu', 'age': 24}
b'\x80\x04\x95"\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x0bsorry seshu\x94\x8c\x03age\x94K\x18u.'
<class 'bytes'>

#reading json data into file by using loads:
with open('man.txt','r') as file:
    import json
    jd=file.read()
    print(jd)
    pd=json.loads(jd)
    print(pd)

#output
{"name": "manoj", "age": 24, "mobile": [1025, 96385], "male": true, "femal": false, "gf": null}
{'name': 'manoj', 'age': 24, 'mobile': [1025, 96385], 'male': True, 'femal': False, 'gf': None}

#reading json data into file by using load:
with open('man.txt','r') as file:
    import json
    jd=json.load(file)
    print(jd)
#output
{'name': 'manoj', 'age': 24, 'mobile': [1025, 96385], 'male': True, 'femal': False, 'gf': None}


#writing json data into file by using dump:
with open('man.txt','w') as file:
    import json
    d={'name':'manoj','age':24,'mobile':(1025,96385),'male':True,'femal':False,'gf':None}
    jd=json.dump(d,file)
    
#output
{"name": "manoj", "age": 24, "mobile": [1025, 96385], "male": true, "femal": false, "gf": null}
#writing json data into file by using dumps:

with open('man.txt','w') as file:
    import json
    d={'name':'manoj','age':24,'mobile':(1025,96385),'male':True,'femal':False,'gf':None}
    jd=json.dumps(d)
    file.write(jd)
output:
{"name": "manoj", "age": 24, "mobile": [1025, 96385], "male": true, "femal": false, "gf": null}

#with keyword
with open('man.txt','w') as file:
    file.write('this is with key word')

#attributes and IMPOERTANT methods
fo=open("manoj.txt",'w')
print(fo.name)
print(fo.mode)
print(fo.closed)
print(fo.writable())
print(fo.readable())
#output
manoj.txt
w
False
True
False

fo=open("manoj.txt",'r')
print(fo.name)
print(fo.mode)
print(fo.closed)
print(fo.writable())
print(fo.readable())
#output
manoj.txt
r
False
False
True


#read mode
1. read
fo=open("manu.txt",'r')
data=fo.read()
print(data)
print(type(data))

2.readline
fo=open("manu.txt",'r')
data=fo.readline(150)
print(data)
print(type(data))

3.readlines
fo=open("manu.txt",'r')
data=fo.readlines()
print(data)
print(type(data))


ex:read
fo=open("manu.txt",'r')
data=fo.read()
print(data)
print(type(data))
print(fo.tell())
fo.seek(1156)
print(fo.tell())
data1=fo.read()
print(data1)
print(type(data1))

ex:readline
fo=open("manu.txt",'r')
data=fo.readline(150)
print(data)
print(type(data))
print(fo.tell())
fo.seek(15)
print(fo.tell())
data1=fo.readline(50)
print(data1)
print(type(data1))

ex:readlines
fo=open("manu.txt",'r')
data=fo.readlines()
print(data)
print(type(data))
print(fo.tell())
fo.seek(15)
print(fo.tell())
data1=fo.readlines()
print(data1)
print(type(data1))*9

#append
fo=open("manu.txt",'a')
fo.writelines(["Virender Sehwag has constructed an extraordinary\n "
               "career with a relentless quest, and a genius\n",
               "for boundary hitting. With minimal footwork but maximum intent\n",
               "he has piled Test runs at a faster pace than anyone in the history of cricket.\n"
               'Bowlers must always fancy their chances against\n'
               'a batsman who plays so many strokes \n',
               "its just that Sehwag fancies his chances against them much more.\n"])
#fo.writelines({"name ":'manoj','mobile ':9866847308,'age ':24})
fo.close()

#write mode
1.write method

fo=open("manoj.txt",'w')
fo.write("hai manoj how r u ?")
fo.close()
2 . writelines method
fo=open("manoj.txt",'w')
#fo.writelines(["seshu is a comedian "])
fo.writelines({"name ":'manoj','mobile':9866847308,'age':24})
fo.close()

'''
