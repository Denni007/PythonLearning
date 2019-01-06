def rev():
    '''this is programme of reverse number'''
    x=input("enter the number")
    re=0
    while(x>0):
        x=eval(x)
        a=x%10
        re=(re*10)+a
        x=x//10
    print(rev)
rev()
