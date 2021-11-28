salario_atual = float(input("Informe o salário do funcionário: "))
tempo_servico = int(input("Informe o tempo de serviço (em anos): "))

if salario_atual <= 500:
    salario_atual = salario_atual * 1.25
elif salario_atual <= 1000:
    salario_atual = salario_atual * 1.20
elif salario_atual <= 1500:
    salario_atual = salario_atual * 1.15
elif salario_atual <= 2000:
    salario_atual = salario_atual * 1.10
elif salario_atual > 2000:
    print("Não haverá reajuste")
else:
    print("Valores inválidos")

if tempo_servico < 1:
    print("Não haverá bônus")
elif 1 <= tempo_servico < 3:
    salario_atual = salario_atual + 100
elif 3 <= tempo_servico < 6:
    salario_atual = salario_atual + 200
elif 6 <= tempo_servico < 10:
    salario_atual = salario_atual + 300
elif tempo_servico >= 10:
    salario_atual = salario_atual + 500
else:
    print("Valores inválidos")

print(f"O salário reajustado será R$ {salario_atual}")