def extract(s):
    t=0
    v="AEIOU"
    s=s.upper()
    for i in s:
        if i in v:
            t+=ord(i)-32
    return t
            
x=extract("ajnkaeeisdciauo")
print(x)
