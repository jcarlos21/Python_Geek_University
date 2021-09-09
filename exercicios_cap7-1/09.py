"""
Questão 09
"""
vetor = []
valor = 0
print('Entre com os valores pares do vetor de 6 elementos:')
for i in range(0, 6):
    valor = int(input(f'Entre com {i+1}: '))
    while valor % 2 != 0:
        valor = int(input(f'Entre com um número par!!! Digite o  {i + 1} valor: '))
    vetor.append(valor)

print(f'O vetor na ordem inversa é: {vetor[::-1]}.')
