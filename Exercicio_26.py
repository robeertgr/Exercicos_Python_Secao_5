dist = float(input("Digite a distância percorrida em quilômetros: "))
litros = float(input("Digite o consumo de gasolina do percuso (em litros): "))

consumo = dist / litros

if consumo < 8:
    print("Venda o carro!")

elif 8 < consumo < 12:
    print("Econômico.")

else:
    print("Super econômico.")