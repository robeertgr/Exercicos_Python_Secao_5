print("Escolha a opção:\n"
      "1- Soma de 2 números\n"
      "2- Diferença entre 2 números (maior pelo menor)\n"
      "3- Produto entre 2 números\n"
      "4- Divisão entre 2 números (o denominador não pode ser zero)")
opcao = int(input("Opção: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    total = num1 + num2
    print(f"Resultado: {round(total, 2)}")
elif opcao == 2:
    if num1 > num2:
        total = num1 - num2
        print(f"Resultado: {round(total, 2)}")
    else:
        total = num2 - num1
        print(f"Resultado: {round(total, 2)}")
elif opcao == 3:
    total = num1 * num2
    print(f"Resultado: {round(total, 2)}")
elif opcao == 4:
    if num2 == 0:
        print(f"O denomiador não pode ser 0")
    else:
        total = num1 / num2
        print(f"Resultado: {round(total, 2)}")
else:
    print("Opções inválidas")
