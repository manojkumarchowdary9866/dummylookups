def remove(n1,n2):
    t=0
    for i in n1:
        if i==n2:
            t+=1
    return t

def re(d):
    t=""
    for i in d:
        if i not in t:
            t+=i
    return t

def echr(d):
    s1=re(d)
    for i in s1:
        print(f'{i} = {d.count(i)}')

x=echr("we are python developers")
print(x)
