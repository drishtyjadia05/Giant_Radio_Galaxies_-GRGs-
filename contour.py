import numpy as np

a = input("provide sigma")
a = float(a)

c = 3*a
c = float(c)

print("3 sigma",c)

b = input("provide f_max")
b = float(b)

while c <= b:
    print(c)
    c = c*np.sqrt(2)

