print("Médias de acordo\n"
      "A- Geométrica\n"
      "B- Ponderada\n"
      "C- Harmônica\n"
      "D- Aritmética")
opcao = input("Opção: ")
x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = float(input("Digite o valor de Z: "))

if opcao == 'A' or opcao == 'a':
    total = (x * y * z) ** (1 / 3)
    print(f"Média geométrica: {round(total, 2)}")
elif opcao == 'B' or opcao == 'b':
    total = (x + 2 * y + 3 * z) / 6
    print(f"Média ponderada: {round(total, 2)}")
elif opcao == 'C' or opcao == 'c':
    total = 1 / ((1 / x) + (1 / y) + (1 / z))
    print(f"Média harmônica: {round(total, 2)}")
elif opcao == 'D' or opcao == 'd':
    total = (x + y + z) / 3
    print(f"Média aritmética: {round(total, 2)}")
else:
    print("Opção inválida.")
