print("Especificação        Código      Preço\n"
      "Cachorro Quente      100         1.20\n"
      "Bauru Simples        101         1.30\n"
      "Bauru com Ovo        102         1.50\n"
      "Hamburguer           103         1.20\n"
      "Cheeseburguer        104         1.70\n"
      "Suco                 105         2.20\n"
      "Refrigerante         106         1.00")
codigo = int(input("Digite o código: "))
qntd = int(input("Digite a quantidade: "))

if codigo == 100:
    total = qntd * 1.20
    print(f"Preço total de {qntd} unidades: R$ {round(total, 2)}")
elif codigo == 101:
    total = qntd * 1.30
    print(f"Preço total de {qntd} unidades: R$ {round(total, 2)}")
elif codigo == 102:
    total = qntd * 1.50
    print(f"Preço total de {qntd} unidades: R$ {round(total, 2)}")
elif codigo == 103:
    total = qntd * 1.20
    print(f"Preço total de {qntd} unidades: R$ {round(total, 2)}")
elif codigo == 104:
    total = qntd * 1.70
    print(f"Preço total de {qntd} unidades: R$ {round(total, 2)}")
elif codigo == 105:
    total = qntd * 2.20
    print(f"Preço total de {qntd} unidades: R$ {round(total, 2)}")
elif codigo == 106:
    total = qntd * 1.00
    print(f"Preço total de {qntd} unidades: R$ {round(total, 2)}")
else:
    print("Código inválido!")
