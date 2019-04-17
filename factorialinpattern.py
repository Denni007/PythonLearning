def fact1(n):
    if n>1:
        r=fact1(n-1)*n
        return r
    elif n==0:
        return 1
    else:
        return 1
        
for i in range(6,0,-1):
    for j in range(i-1):
        print("    ",end=" ")
    print("fact",i-1)
  
for i in range(0,6):
    for j in range(i):
        print("    ",end=" ")
    print("fact",fact1(i))
    
     
