s="maanaooaaahaaahhddd"
d={}
for i in s:
    d[i]=s.count(i)
print(d)
'''for i in d:
    print(f'{i} = {d[i]}')'''
for k,v in d.items():
    print(f'{k} = {v}')
