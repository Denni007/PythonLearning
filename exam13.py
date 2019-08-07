count=[]
def add(c):
    if(c in count):
        count[c]+=1
    else:
        count[c]=1


add('china')
#add(China)
#add(Japan)
print(len(count))