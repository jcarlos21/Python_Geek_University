"""
Questão 35
"""
print('Digite um valor inicial e valor final: ')
vi = int(input('Valor incial: '))
vf = int(input('Valor final: '))
soma = 0
if vi < vf:
    for i in range(vi, vf+1):
        if i % 2 == 1:
            soma += i
    print(f'Soma dos ímpares neste intervalo: {soma}')
else:
    print('Intervalo de valores inválido! ')
