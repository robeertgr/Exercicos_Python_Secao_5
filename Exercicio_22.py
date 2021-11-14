idade = int(input("Digite a idade do trabalhador:"))
tempo = int(input("Digite o tempo de serviço do trabalhador (em anos):"))

if idade == 65 or idade < 65 and tempo >= 30 or idade >= 60 and tempo >= 25:
    print("Apto para aposentadoria.")

else:
    print("Inapto para aposentadoria.")