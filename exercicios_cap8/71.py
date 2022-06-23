"""
Questão 71
"""


def dentroRet(x1, y1, x2, y2, px, py):
    cont = 0
    if abs(x2) >= abs(px) >= abs(x1):
        cont += 1
    if abs(y2) >= abs(py) >= abs(y1):
        cont += 1
    if cont == 2:
        return True
    return False


print(round(2.3525445, 2))  # teste

print('Entre com os dois pontos equivalentes ao retângulo: ')
retx1 = int(input('Coordenada x1: '))
rety1 = int(input('Coordenada y1: '))
retx2 = int(input('Coordenada x2: '))
rety2 = int(input('Coordenada y2: '))

print('Entre com o ponto a ser pesquisado no retângulo:')
pontox = int(input('Entre com a coordenada x do ponto: '))
pontoy = int(input('Entre com a coordenada y do ponto: '))
if dentroRet(retx1, rety1, retx2, rety2, pontox, pontoy):
    print(f'O ponto ({pontox},{pontoy}) está dentro do retângulo.')
else:
    print(f'O ponto ({pontox},{pontoy}) não está dentro do retângulo.')

