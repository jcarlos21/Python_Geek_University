"""
Questão 18
"""
vetor = []
valor = 0

for i in range(0, 10):
    valor = int(input(f'Entre com {i+1}° valor real: '))
    vetor.append(valor)

cont = 0
x = int(input('Entre com um número inteiro: '))
vetor1 = []
for j in range(0, len(vetor)):
    if vetor[j] % x == 0:
        cont += 1
        vetor1.append(vetor[j])
vetor1.sort()
print(f'O vetor de multiplos de {x} é {vetor1} e possui {cont} ocorrências.')
