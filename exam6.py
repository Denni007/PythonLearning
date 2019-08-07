def convet(a):
    if(a>1):
        convet(a//2)
    print(a%2,end="")
n=15
convet(n)
