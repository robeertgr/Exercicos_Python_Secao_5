print("CALCULADORA")
print("+ Soma")
print("- Subtração")
print("* Multiplicação")
print("/ Divisão")

operacao = input("Informe o símbolo da operação: ")
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

if operacao == '+':
    print(f"Soma: {numero1 + numero2}")
elif operacao == '-':
    print(f"Subtração: {numero1 - numero2}")
elif operacao == '*':
    print(f"Multiplicação: {numero1 * numero2}")
elif operacao == '/':
    print(f"Divisão: {numero1 / numero2}")
else:
    print("Operação inválida.")
