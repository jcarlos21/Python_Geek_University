"""
Questão 05
"""
a = 0
soma = 0
for i in range(0, 10):
    a = int(input(f'Entre com o {i+1}° valor: '))
    soma = soma + a
print(f'\nA soma dos números digitados é igual: {soma}')
