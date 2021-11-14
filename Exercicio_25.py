import math

print("Cálculo de equação do segundo grau.")
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

delta = math.pow(b, 2) - 4 * a * c

if a == 0:
    print("Não é equação do segundo grau!")
elif delta < 0:
    print("Não existe raiz.")
elif delta == 0:
    print(f"Raíz única: {round(delta, 2)}")
elif delta > 0:
    x1 = (-b + (math.sqrt(delta))) / (2 * a)
    x2 = (-b - (math.sqrt(delta))) / (2 * a)
    print(f"Duas raízes:\n"
          f"x1: {round(x1, 2)}\n"
          f"x2: {round(x2, 2)}")
else:
    print("Valores inválidos.")
