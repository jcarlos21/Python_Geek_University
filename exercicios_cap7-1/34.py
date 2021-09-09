"""
Questão 34
"""
vetor = []
valor = 0
for i in range(0, 10):
    valor = int(input(f'Entre em com {i + 1}° valor: '))
    while vetor.count(valor) == 1:
        valor = int(input(f'Valor já foi digitado anteriormente! Entre com um valor diferente para {i + 1}°: '))
    vetor.append(valor)
print(f'\nO vetor digitado é: {vetor}')
