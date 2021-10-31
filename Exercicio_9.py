salario = float(input("Digite o salário do trabalhador: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

if prestacao < salario * 0.20:
    print("Empréstimo condecido")
else:
    print("Empréstimo não concedido")
