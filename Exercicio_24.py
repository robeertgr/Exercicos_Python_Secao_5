valor = float(input("Informe o valor: "))
print("Informe o estado:\n"
      "1- MG 7%\n"
      "2- SP 12%\n"
      "3- RJ 15%\n"
      "4- MS 8%")
opcao = int(input("Opcao: "))

if opcao == 1:
    total = valor * 1.07
    print(f"Valor com imposto: {round(total, 2)}")
elif opcao == 2:
    total = valor * 1.12
    print(f"Valor com imposto: {round(total, 2)}")
elif opcao == 3:
    total = valor * 1.15
    print(f"Valor com imposto: {round(total, 2)}")
elif opcao == 4:
    total = valor * 1.08
    print(f"Valor com imposto: {round(total, 2)}")
else:
    print("Opção inválida.")
