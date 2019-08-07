l=[13,1,2,13,1,13,13,13,13,2,13]
for i in range(len(l)):
    if (l[i]==13):
        l[i]=0
        if (i!=len(l)-1 and l[i+1]!=13):
            a=i+1
            l[a]=0
print(sum(l))
