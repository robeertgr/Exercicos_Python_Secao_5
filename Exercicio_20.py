a = int(input("Informe o valor A: "))
b = int(input("Informe o valor B: "))
c = int(input("Informe o valor C: "))

if b + c < a:
    print("O valor inserido em 'A' não pode ser maior que a soma de 'B' + 'C'")

elif a + c < b:
    print("O valor inserido em 'B' não pode ser maior que a soma de 'A' + 'C'")

elif a + b < c:
    print("O valor inserido em 'C' não pode ser maior que a soma de 'B' + 'A'")

elif a == b == c:
    print("O triângulo é equilátero.")
elif a == b != c or a == c != b or c == b != a:
    print("O triângulo é isosceles.")
else:
    print("O triângulo é escaleno.")
