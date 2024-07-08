from math import sqrt

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = (-b) ** 2 - 4 * a * c

print()
print("delta = ", delta)
print()

if delta < 0:
    print("Pas de solution réele ")
    reponse = input("Voulez-vous voir les solutions complexes ? (o/n) : ")
    if reponse == "o":
        x1 = ((-b) - sqrt(-delta)*1j) / (2 * a)
        x2 = ((-b) + sqrt(-delta)*1j) / (2 * a)
        print("S = {", str(x1)[1:-2], "i ; ", str(x2)[1:-2], "i}", sep="")
elif delta == 0:
    x0 = (-b) / (2 * a)
    print("S = {", x0, "}")
elif delta > 0:
    x1 = ((-b) - sqrt(delta)) / (2 * a)
    x2 = ((-b) + sqrt(delta)) / (2 * a)
    print("S = {", x1, ";", x2, "}")
