from math import *

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = (-b) ** 2 - 4 * a * c

print()
print("delta = ", delta)
print()

if delta < 0:
    print("Pas de solution dans |R")
elif delta == 0:
    x0 = (-b) / (2 * a)
    print("S = {", x0, "}")
elif delta > 0:
    x1 = ((-b) - sqrt(delta)) / (2 * a)
    x2 = ((-b) + sqrt(delta)) / (2 * a)
    print("S = {", x1, ";", x2, "}")
