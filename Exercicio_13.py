nota1 = float(input("Digite a nota do laboratório: "))
nota2 = float(input("Digite a nota da avaliação semestral: "))
nota3 = float(input("Digite a nota do exame final: "))

mediaPonderada = ((nota1 + nota2 + (nota3 * 2)) / 4) * 10

if mediaPonderada > 60:
    print(f"Aluno aprovado com uma media de {mediaPonderada}.")
else:
    print(f"Aluno reprovado com uma media de {mediaPonderada}.")
