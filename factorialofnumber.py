def fact():
    '''this is the factorial number orogram'''
    a, b = 0, 1
    n=input("enter the number of fibo")
    d=eval(n)
    while a < d:
        print(a, end=' ')
        a, b = b, a+b
    print()
fact()
