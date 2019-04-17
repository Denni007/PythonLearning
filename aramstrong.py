def armstrong(x):
    temp=x
    
    if(x>0):
        b=0
        i=len(str(x))
        while x>0:
            a = x%10
            b = b+a**i
            x = x//10
        if b == temp:
            return b
        else:
            return 0
    else:
        return 0
n=int(input("enter the number is range"))
l=list(filter(armstrong,range(1,n+1)))
#for i in range(0,l.count(0)):
#    l.remove(0)
     
    
print("armstrong number:",l)
