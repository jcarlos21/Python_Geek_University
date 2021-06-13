"""
Questão 17
"""
BaseMaior = input('Entre com a base maior (valor deve ser maior que zero): ')
BaseMenor = input('Entre com a base menor (valor deve ser maior que zero): ')
Altura = input('Entre com a altura: ')

while not BaseMaior.isdigit() or not BaseMenor.isdigit() or not Altura.isdigit() or not (float(BaseMenor) > 0 and float(BaseMenor) > 0):
    print('\nOs valores digitados não correspondem ao esperado. Por favor digite-os novamente!\n')
    BaseMaior = input('Base maior: ')
    BaseMenor = input('Base menor: ')
    Altura = input('Altura: ')

print(f'A área do trapézio: {(((float(BaseMaior) + float(BaseMenor)) * float(Altura)) / 2).__round__(2)}')
