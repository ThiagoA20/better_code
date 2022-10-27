x = lambda a: a + 10

print(x(25))
print(x(100))
print(x(-10))

y = lambda a, b, c: a * b + c

print(y(3, 4, 26))

def multiplyFuntionFactory(n):
    return lambda a: a * n

doubleFunction = multiplyFuntionFactory(2)
tripleFunction = multiplyFuntionFactory(3)

value = 10
print(doubleFunction(value))
print(tripleFunction(value))