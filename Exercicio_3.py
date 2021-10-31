import math

num = float(input("Informe um número: "))

if num > 0:
    num = math.sqrt(num)
    print(num)
else:
    num = pow(num, 2)
    print(num)
