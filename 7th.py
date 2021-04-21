# given a postive number,print its fraction part
import math
value = float(input('enter any number'))
x, a = math.modf(value)
print(x)