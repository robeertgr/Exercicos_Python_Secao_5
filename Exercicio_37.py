entrada = input('Hora de entrada separada por ":": ')
saida = input('Hora saída separada por ":": ')

valor = 0

# Calculando o minuto de entrada
hora_entrada, minuto_entrada = entrada.split(':')
t_entrada = (int(hora_entrada) * 60) + int(minuto_entrada)

# hora saida
hora_saida, minuto_saida = saida.split(':')
hora_saida = int(hora_saida.replace('00', '24'))

if hora_saida < int(hora_entrada):
    t_saida = ((int(hora_saida) + 24) * 60) + int(minuto_saida)
else:
    t_saida = (hora_saida * 60) + int(minuto_saida)

if ((t_saida - t_entrada).__divmod__(60))[1] > 0:
    periodo = ((t_saida - t_entrada).__divmod__(60))[0] + 1
else:
    periodo = ((t_saida - t_entrada).__divmod__(60))[0]

if periodo <= 2:
    valor += periodo * 1
elif 2 < periodo <= 4:
    valor += 2 * 1
    valor += (periodo - 2) * 1.40
else:
    valor += 2 * 1
    valor += 2 * 1.40
    valor += (periodo - 4) * 2

print(f'Valor cobrado é de R${valor} referente a {periodo} hora(s), do perido de {entrada} as {saida}.')
