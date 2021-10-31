num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    dif = num1 - num2
    print(f"O número {num1} é o maior que {num2} e sua diferença para o número 2 é {dif}")
else:
    dif = num2 - num1
    print(f"O número {num2} é o maior que {num1} e sua diferença para o número 2 é {dif}")
