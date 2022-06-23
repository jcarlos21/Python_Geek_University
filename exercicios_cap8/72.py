"""
Questão 72
"""


def SomaVetor(vetor1, vetor2):
    vetor3 = []
    for a in range(0, len(vetor1)):
        vetor3.append(vetor1[a]+vetor2[a])
    return vetor3


print('Entre com dois vetores tridimensionais: ')
x1 = int(input('Coordenada x1:'))
y1 = int(input('Coordenada y1:'))
z1 = int(input('Coordenada z1:'))
x2 = int(input('Coordenada x2:'))
y2 = int(input('Coordenada y2:'))
z2 = int(input('Coordenada z2:'))

v1 = [x1, y1, z1]
v2 = [x2, y2, z2]

print(f'A soma dos vetores é: {SomaVetor(v1, v2)}')
