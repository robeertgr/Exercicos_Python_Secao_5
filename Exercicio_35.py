dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if 1 <= dia <= 31:
        print(f"Data {dia}/{mes}/{ano} válido.")
    else:
        print(f"Data {dia}/{mes}/{ano} inválido.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if 1 <= dia <= 30:
        print(f"Data {dia}/{mes}/{ano} válido.")
    else:
        print(f"Data {dia}/{mes}/{ano} inválido.")
elif mes == 2:
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        if dia <= 29:
            print(f"Data {dia}/{mes}/{ano} válido.")
        else:
            print(f"Data {dia}/{mes}/{ano} inválido.")
    elif dia <= 28:
        print(f"Data {dia}/{mes}/{ano} válido.")
    else:
        print(f"Data {dia}/{mes}/{ano} inválido.")
else:
    print(f"Data {dia}/{mes}/{ano} inválido.")
