"""
Questão 06
"""
a = 0
soma = 0
cont = 0
for i in range(0, 10):
    a = int(input(f'Entre com o {i+1}° valor: '))
    if a > 0:
        soma = soma + a
        cont += 1
print(f'\nA média dos números digitados é igual: {soma / cont}')
