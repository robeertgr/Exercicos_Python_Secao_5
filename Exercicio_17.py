baseMaior = float(input("Informe a base maior: "))
baseMenor = float(input("Informe a base menor: "))
altura = float(input("Informe a altura: "))

a = ((baseMaior + baseMenor) * altura) / 2

if baseMenor > 0 and baseMaior > 0:
    print(f"A área do trapézio é {round(a, 2)}")
else:
    print("A base maior e a base menor devem ser maiores do que 0.")
