def extract_first_char(s):
    s1=''
    # Write the logic here
    # return first character
    for i in range(len(s)):
        if i==0:
            s1+=s[i]
    return s1
a=extract_first_char(input())
print(a)

# The code below was automatically added to handle input/output operations
'''inp_str = input()
print(extract_first_char(inp_str))'''
