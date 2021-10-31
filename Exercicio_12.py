import math

num = int(input("Digite um número positivo: "))

if num > 0:
    log = math.log(num, 10)
    print(f"O logaritmo de {num} é {round(log, 2)}")
else:
    print("Número inválido.")
