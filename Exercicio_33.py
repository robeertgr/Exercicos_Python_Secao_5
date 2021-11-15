print("Preço antigo                 Percentual de aumento\n"
      "Até R$ 50.00                 5%\n"
      "Entre R$ 50.00 e R$ 100.00   10%\n"
      "Acima de R$ 100.00           15%")
preco = float(input("Informe o valor para saber o aumento: "))

if preco < 50:
      aumento = preco * 1.05
      print(f"Valor com aumento: {round(aumento, 2)}")
elif 50 <= preco <= 100:
      aumento = preco * 1.10
      print(f"Valor com aumento: {round(aumento, 2)}")
elif preco > 100:
      aumento = preco * 1.15
      print(f"Valor com aumento: {round(aumento, 2)}")
else:
      print("Valores inválidos.")

if aumento < 80:
      print("Barato")
elif 80 <= aumento <= 120:
      print("Normal")
elif 120 <= aumento <= 200:
      print("Caro")
elif aumento > 200:
      print("Muito caro")
else:
      print("Valores inválidos.")
