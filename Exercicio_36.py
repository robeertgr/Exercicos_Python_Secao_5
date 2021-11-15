valorVenda = float(input("Informe o valor de venda: "))

if valorVenda >= 100000:
    comissao = 700 + (valorVenda * 1.16)
    print(f"Valor de venda: R$ {valorVenda}\n"
          f"Comissão: R$ {round(comissao, 2) - valorVenda}")
elif 100000 <= valorVenda <= 80000:
    comissao = 650 + (valorVenda * 1.14)
    print(f"Valor de venda: R$ {valorVenda}\n"
          f"Comissão: R$ {round(comissao, 2) - valorVenda}")
elif 80000 <= valorVenda <= 60000:
    comissao = 600 + (valorVenda * 1.14)
    print(f"Valor de venda: R$ {valorVenda}\n"
          f"Comissão: R$ {round(comissao, 2) - valorVenda}")
elif 60000 <= valorVenda <= 40000:
    comissao = 550 + (valorVenda * 1.14)
    print(f"Valor de venda: R$ {valorVenda}\n"
          f"Comissão: R$ {round(comissao, 2) - valorVenda}")
elif 40000 <= valorVenda <= 20000:
    comissao = 500 + (valorVenda * 1.14)
    print(f"Valor de venda: R$ {valorVenda}\n"
          f"Comissão: R$ {round(comissao, 2) - valorVenda}")
elif valorVenda < 20000:
    comissao = 400 + (valorVenda * 1.14)
    print(f"Valor de venda: R$ {valorVenda}\n"
          f"Comissão: R$ {round(comissao, 2) - valorVenda}")
else:
    print("Valores inválidos.")
