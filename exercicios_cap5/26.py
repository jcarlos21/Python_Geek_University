"""
Questão 26
"""
km = float(input('Entre com a distância em quilometros: '))
litros = float(input('Entre com a quantidade consumida pelo carro: '))

consumo = km / litros

if consumo < 8:
    print('Venda o carro!')
elif 8 <= consumo <= 12:  # essa forma substitui o "and"
    print('Econômico!')
else:
    print('Super econômico!')
