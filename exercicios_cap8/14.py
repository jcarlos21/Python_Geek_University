"""
Questão 14
"""


def analiseconsumo(distancia, litros):
    return distancia / litros


kilometragem = float(input('Entre com a kilometragem: '))
consumo = float(input('Entre com a consumo de gasolina: '))

print(f'\nA relação km/l é: {analiseconsumo(kilometragem, consumo)}\n')

if analiseconsumo(kilometragem, consumo) < 8:
    print('Venda o carro!')
elif 14 >= analiseconsumo(kilometragem, consumo) >= 8:
    print('Econômico!')
else:
    print('Super econômico!')
