def fib(n):
    result=1
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
a=5
for i in range(0,a):
    print(fib(i))


