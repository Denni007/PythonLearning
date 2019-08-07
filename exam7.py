flag=0
for i in range(2,100):
    #print(i,"times")
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:        
        print(i)     
        
        
