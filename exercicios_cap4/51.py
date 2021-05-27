"""
Questão 51
"""
import math
print('Cálculo da distância de um ponto com relação a origem (0,0).')
x = int(input('Entre com a coordenada x: '))
y = int(input('Entre com a coordenada y: '))
print(f'A distância é {(math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))).__round__(2)}')
