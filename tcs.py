a=input()

a=a[::-1]
l=[]
sum = 0
for i in range(len(a)):
    if(a[i]=='A'):
        l.append(10)
    elif(a[i]=='B'):
        l.append(11)
    elif(a[i]=='C'):
        l.append(12)
    elif(a[i]=='D'):
        l.append(13)
    elif(a[i]=='E'):
        l.append(14)
    elif(a[i]=='F'):
        l.append(15)
    elif(a[i]=='G'):
        l.append(16)
    else:
        c=a[i]
        l.append(c)
    sum=sum+(17**i)*int(l[i])      
print(sum)
