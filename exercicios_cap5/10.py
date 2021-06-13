"""
Questão 10
"""
h = float(input('Entre com a altura: '))
sexo = input('Entre com  o sexo (M - masculino, F - feminino: ')
while sexo != 'M' and sexo != 'F':
    sexo = input('Valor inválido. Entre com  o sexo (M - masculino, F - feminino: ')
if sexo == 'M':
    print(f'O peso ideal para os homens é: {(72.7 * h) - 58}')
else:
    print(f'O peso ideal para as mulheres é: {(62.1 * h) - 44.7}')
