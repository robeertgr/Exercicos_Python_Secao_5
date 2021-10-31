num = int(input("Digite um número inteiro de 0 a 999: "))
num1 = str(num)

if 100 <= num < 999:
    soma = int(num1[0]) + int(num1[1]) + int(num1[2])
    print(f"A soma dos algarismos de {num} é {soma}")
elif 0 <= num < 100:
    soma = int(num1[0]) + int(num1[1])
    print(f"A soma dos algarismos de {num} é {soma}")
else:
    print("Número inválido.")
