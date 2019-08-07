x=int(input("enter size of array"))
if (x==0):
    print("0")
else:
    a=[]
    print("enter elemet for array")
    i=0
    while i<=x:
        data=int(input("enter elemnt"))
        a.append(data)
        i=i+1
    #doing addition according to condition
    j=0
    result=0
    while j<x:
        if a[j]==13:
            if j==x-1:
                break 
            else:
                j=j+2
        else:
            result=result+a[j]
        j=j+1
    print(result)
