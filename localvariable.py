class A:
    pass
a = A()
a.x = 7
print(a.x)
del a.x
print(a.x)

