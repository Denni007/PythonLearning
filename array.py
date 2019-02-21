from array import *
a = array('i',[1,2,3,4,5])
c=[10,20,30]
b = array('i',[7,8,9,10])

a.append(6)
a.extend(b)
a.fromlist(c)
a.insert(11,0)
a.remove(20)
a.extend(b)
#print(a.index(0))
a.reverse()
for i in a:
    print(i)
z=[[1,2,3],[4,5,6],[7,8,9]]
print(z[0])
