"""
Questão 27
"""
vetor = []
valor = 0


def EPrimo(x):
    cont = 0
    for indice in range(1, x+1):
        if x % indice == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False


for i in range(0, 10):
    valor = int(input(f'Entre com o {i+1}° valor: '))
    vetor.append(valor)

for j in range(0, len(vetor)):
    if EPrimo(vetor[j]):
        print(f'O valor {vetor[j]} é primo e está na posição {j}.')
