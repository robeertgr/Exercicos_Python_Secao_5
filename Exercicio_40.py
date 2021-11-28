custo_fabrica = float(input("Digite o custo de fábrica: "))

if custo_fabrica < 12000:
    custo_total = custo_fabrica * 1.05
elif 12000 <= custo_fabrica <= 25000:
    custo_total = (custo_fabrica * 1.10) + (custo_fabrica * 1.15) - custo_fabrica
elif custo_fabrica > 25000:
    custo_total = (custo_fabrica * 1.15) + (custo_fabrica * 1.20) - custo_fabrica
else:
    print("Valores inválidos")

print(f"O custo ao consumidor será R$ {custo_total}")
