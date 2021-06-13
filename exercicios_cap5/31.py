"""
Questão 31
"""
Altura = float(input('Entre com a altura: '))
Peso = float(input('Entre com o peso: '))

if Altura < 1.20:
    if Peso < 60:
        print('A pessoa tem classificação A')
    elif 60 <= Peso <= 90:  # Simplificação do operador "and"
        print('A pessoa tem classificação D')
    else:
        print('A pessoa tem classificação G')
elif 1.20 <= Altura <= 1.70:
    if Peso < 60:
        print('A pessoa tem classificação B')
    elif 60 <= Peso <= 90:  # Simplificação do operador "and"
        print('A pessoa tem classificação E')
    else:
        print('A pessoa tem classificação H')
else:
    if Peso < 60:
        print('A pessoa tem classificação C')
    elif 60 <= Peso <= 90:  # Simplificação do operador "and"
        print('A pessoa tem classificação F')
    else:
        print('A pessoa tem classificação I')
