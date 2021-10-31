altura = float(input("Informe a altura:"))
sexo = input("Informe o sexo (M ou F):")

if sexo == 'F' or 'f':
    pesoideal = (62.1*altura) - 44.7
    print("O peso ideal é", round(pesoideal, 2))

elif sexo == 'M' or 'm':
    pesoideal = (62.1*altura) - 44.7
    print("O peso ideal é", round(pesoideal, 2))

else:
    print("Valores inválidos.")
