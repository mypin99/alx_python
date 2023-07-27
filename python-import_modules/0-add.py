4-raise_exception.py
import add_0

a = 1
b = 2

result = add_0.add(a, b)
print("{a} + {b} = {result}".format(a=a, b=b, result=result))

a = 10
b = 30

result = add_0.add(a, b)
print("{a} + {b} = {result}".format(a=a, b=b, result=result))

a = -10
b = 30

result = add_0.add(a, b)
print("{a} + {b} = {result}".format(a=a, b=b, result=result))

a = -10
b = -30

result = add_0.add(a, b)
print("{a} + {b} = {result}".format(a=a, b=b, result=result))

a = 5
b = "H"

result = add_0.add(a, b)
print("{a} + {b} = {result}".format(a=a, b=b, result=result))
