"""
Questão 37
"""
A = []
A_novo = []
valor = 0
for i in range(0, 11):
    valor = int(input(f'Entre com o {i + 1}° valor: '))
    A.append(valor)

A.sort()
for j in range(len(A) - 1, 4, -1):  # O vetor A_novo está recebendo os elementos de A (a partir do índice 5 e na ordem inversa)
    A_novo.append(A[j])

num = 0
for m in range(5, len(A)):  # O vetor A está recebendo os elementos de A_novo (a partir do índice 0, ou seja, na ordem direta)
    A[m] = A_novo[num]
    num += 1

print(f'\nO vetor digitado é: {A}')
print(f'\nO vetor novo é: {A_novo}')
