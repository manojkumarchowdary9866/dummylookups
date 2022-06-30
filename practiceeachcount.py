s='ameerbhasa'
s1=''
for i in s:
    if i not in s1:
        s1+=i
        print(f'{i}={s.count(i)}')
