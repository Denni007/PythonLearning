a='hello world!123'
c=0
d=0
for i in a:
    if(i.isdigit()==True):
        c+=1
    if(i.isalpha()==True):
        d+=1
print("lettere",d)
print("digit",c)
