def countvowels(n):
    n=n.upper()
    v="AEIOU"
    c=0
    for i in  n:
        if i in v:
            c+=1
    return c

a=countvowels("mounika")
print(a)
