n=int(input("enter the number"))
y=int(n**0.5)
for i in range(2,y+1):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")
    
