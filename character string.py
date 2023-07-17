s="abcde 12345"
u,l,d,sp=0,0,0,0
for i in range(0,len(s)):
    if s[i].isupper():
        print("upper=",s[i])
        u=u+1
    elif s[i].islower():
        print("lower=",s[i])
        l=l+1
    elif s[i].isdigit():
        print("digit=",s[i])
        d=d+1
    elif s[i].isspace():
        print("space=",s[i])
        sp=sp+1
    else:
        continue
    
print("no.of upper=",u)
print("no.of lower=",l)
print("no.of digit=",d)
print("no.of space=",sp)
