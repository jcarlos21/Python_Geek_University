"""
Questão 02
"""

lista = []
i = 0
valor = 0
while i < 6:
    valor = int(input(f'Entre com o {i+1}° valor: '))
    lista.append(valor)
    i += 1

print(f'\nOs valores lidos foram: {lista}')
lista.sort()
print(f'\nOs valores lidos foram em ordem ficam: {lista}')
