preco_ant = float(input("Digite o preço antigo do produto: "))
aumento = 0
preco_novo = preco_ant * aumento

if preco_ant < 50:
    aumento = 1.05
    preco_novo = preco_ant * aumento
    print(f"O preço novo com 5% de aumento é de {round(preco_novo, 2)}.\n"
          f"BARATO")

elif 50 <= preco_ant <= 100 and preco_novo < 80 :
    aumento = 1.1
    preco_novo = preco_ant * aumento
    print(f"O preço novo com 10% de aumento é de {round(preco_novo, 2)}.\n"
          f"BARATO")

elif 50 <= preco_ant <= 100 and 80 <= preco_novo < 120:
    aumento = 1.1
    preco_novo = preco_ant * aumento
    print(f"O preço novo com 10% de aumento é de {round(preco_novo, 2)}.\n"
          f"NORMAL")

elif preco_ant > 100 and 80 <= preco_novo < 120:
    aumento = 1.5
    preco_novo = preco_ant * aumento
    print(f"O preço novo com 15% de aumento é de {round(preco_novo, 2)}.\n"
          f"NORMAL")

elif preco_ant > 100 and 120 <= preco_novo <= 200:
    aumento = 1.5
    preco_novo = preco_ant * aumento
    print(f"O preço novo com 15% de aumento é de {round(preco_novo, 2)}.\n"
          f"CARO")

elif preco_ant > 100 and preco_novo > 200:
    aumento = 1.5
    preco_novo = preco_ant * aumento
    print(f"O preço novo com 15% de aumento é de {round(preco_novo, 2)}.\n"
          f"MUITO CARO")

else:
    print("Valores inválidos.")