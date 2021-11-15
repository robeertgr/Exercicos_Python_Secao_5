print("                               Peso\n"
      "Altura           Até 60kg    60 a 90     Acima de 90\n"
      "Menor que 1.20   A           D           G\n"
      "De 1.20 a 1.70   B           E           H\n"
      "Maior que 1.70   C           F           I")

peso = float(input("Informe o peso da pessoa: "))
altura = float(input("Informe a altura da pessoa: "))

if peso < 60 and altura < 1.20:
    print("Classificação: A")
elif 60 <= peso <= 90 and altura < 1.20:
    print("Classificação: D")
elif peso > 90 and altura < 1.20:
    print("Classificação: G")
elif peso < 60 and 1.20 <= altura <= 1.70:
    print("Classificação: B")
elif 60 <= peso <= 90 and 1.20 <= altura <= 1.70:
    print("Classificação: E")
elif peso > 90 and 1.20 <= altura <= 1.70:
    print("Classificação: H")
elif peso < 60 and altura > 1.70:
    print("Classificação: C")
elif 60 <= peso <= 90 and altura > 1.70:
    print("Classificação: F")
elif peso > 90 and altura > 1.70:
    print("Classificação: I")
else:
    print("Valores inválidos.")
