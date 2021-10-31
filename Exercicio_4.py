import math

num = float(input("Digite um número: "))

if num > 0:
    quadrado = pow(num, 2)
    raiz = math.sqrt(num)
    print(f"O quadrado de {num} é {round(quadrado, 2)}\n"
          f"A raiz de {num} é {round(raiz, 2)}")
else:
    print("Número inválido")
