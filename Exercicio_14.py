notaLab = float(input("Digite a nota do laboratório: "))
notaAvalSem = float(input("Digite a nota da avaliação semestral: "))
notaExame = float(input("Digite a nota do exame final: "))

mediaPonderada = ((notaLab * 2) + (notaAvalSem * 3) + (notaExame * 5)) / 10

if 0 <= mediaPonderada <= 2.9:
    print(f"Aluno reprovado com uma média de {mediaPonderada}")
elif 3 <= mediaPonderada <= 4.9:
    print(f"Aluno em recuperação com uma média de {mediaPonderada}")
else:
    print(f"Aluno aprovado com uma média de {mediaPonderada}")
