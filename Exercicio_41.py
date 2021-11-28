import math

peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))

imc = peso / math.pow(altura, 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.6 <= imc <= 24.9:
    print("Saudável")
elif 25 <= imc <= 29.9:
    print("Peso em excesso")
elif 30 <= imc <= 34.9:
    print("Obesidade grau 1")
elif 35 <= imc <= 39.9:
    print("Obesidade grau 2 (severa)")
elif imc >= 40:
    print("Obesidade grau 3 (mórbida)")
else:
    print("Valores inválidos")

print(f"IMC: {imc:.2f}")
