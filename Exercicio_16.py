"""
mes = int(input("Digite um número de mês entre 1 e 12: "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Mês incorreto")
"""

num = int(input("Informe um número para o mês: "))

mes = ["Janeiro",
       "Fevereiro",
       "Março",
       "Abril",
       "Maio",
       "Junho",
       "Julho",
       "Agosto",
       "Setembro",
       "Outubro",
       "Novembro",
       "Dezembro"]

if 1 < num > 12:
    print("Mês inválido!")
else:
    print(f"O mês escolhido foi {mes[num-1]}")
