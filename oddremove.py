l = [2,15,7,12,15,5,10,23]
for i in l[:]:
    print(i)
    if i%2!=0:
        l.remove(i)   
print(l)
    
