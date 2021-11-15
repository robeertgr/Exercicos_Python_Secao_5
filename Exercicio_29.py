count = 0
acertos = 0

print("Prova de matemática")

while count < 5:
    num1 = int(input("Informe um número entre 1 e 100: "))
    num2 = int(input("Informe um número entre 1 e 100: "))
    if 0 < num1 < 100 and 0 < num2 < 100:
        print(f"Qual o resultado de {num1} + {num2}?")
        respCerta = num1 + num2
        respAluno = int(input("Resposta: "))
        if respAluno == respCerta:
            print(f"Resposta correta! {respCerta}")
            acertos = acertos + 1
        else:
            print(f"Resposta errada! A resposta correta é {respCerta}")
    else:
        print("Número inválido")
    count = count + 1

print(f"Total de acertos: {acertos}")
