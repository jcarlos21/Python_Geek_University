""""
Questão 41
"""

print('\nCÁLCULO DO IMC\n')
Peso = float(input('Entre com o peso: '))
Altura = float(input('Entre com a altura: '))

if Peso / (Altura ** 2) < 18.5:
    print('Abaixo do Peso')
elif 18.6 <= Peso / (Altura ** 2) <= 24.9:
    print('Saudável')
elif 25.0 <= Peso / (Altura ** 2) <= 29.9:
    print('Peso em excesso')
elif 30.0 <= Peso / (Altura ** 2) <= 34.9:
    print('Obesidade Grau I')
elif 35.0 <= Peso / (Altura ** 2) <= 39.9:
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (mórbida)')

