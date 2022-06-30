def count(s,s2):
    t=0
    for i in s:
        if i==s2:
            t+=1
    return t
def removeduplicates(s):
    s2=""
    for i in s:
        if i not in s2:
            s2+=i
    return s2
def counteach(s):
    s1=removeduplicates(s)
    print("s1:",s1)#engir
    for i in s1:
        print(f' {i} = {s.count(i)}')


counteach("engineering")#engir
