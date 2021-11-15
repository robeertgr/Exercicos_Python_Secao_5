print("Nota             Conceito (até 20 faltas)    Conceito (mais de 20 faltas)\n"
      "9.0 até 10.0     A                           B\n"
      "7.5 até 8.9      B                           C\n"
      "5.0 até 7.4      C                           D\n"
      "4.0 até 4.9      D                           E\n"
      "0.0 até 3.9      E                           E")
nota = float(input("Informe a nota do aluno: "))
faltas = int(input("Informe as faltas do aluno: "))

if 9 <= nota <= 10 and faltas < 20:
    print("Conceito A")
elif 9 <= nota <= 10 and faltas >= 20:
    print("Conceito B")
elif 7.5 <= nota <= 8.9 and faltas < 20:
    print("Conceito B")
elif 7.5 <= nota <= 8.9 and faltas >= 20:
    print("Conceito C")
elif 5 <= nota <= 7.4 and faltas < 20:
    print("Conceito C")
elif 5 <= nota <= 7.4 and faltas >= 20:
    print("Conceito D")
elif 4 <= nota <= 4.9 and faltas < 20:
    print("Conceito D")
elif 4 <= nota <= 4.9 and faltas >= 20:
    print("Conceito E")
elif 0 <= nota <= 3.9 and faltas < 20:
    print("Conceito E")
elif 0 <= nota <= 3.9 and faltas >= 20:
    print("Conceito E")
else:
    print("Valores inválidos.")
