def nlist(a):
    li=[]
    for i in a:
        if i not in li:
            li.append(i)
    return li
a=[1,2,3,1,2,2,1,2,3,4,5]

a=nlist(a)
print(a)
