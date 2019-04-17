n=input("enter the word:")
b=[]
for i in n:
    b.append(i)
print(b)
y=len(b)
for i in range(0,y):
    x=y
    for j in range(i+1,x):
        if (b[i]==b[j]) and i!=j:
            b.insert(j,0)
            
for i in range(len(b)):
    if(b.index(i)==0):
        del b[i]
print(b)
