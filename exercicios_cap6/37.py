"""
Questão 37
"""
inicio = 0
fim = 0
quadrado = 0
lista = []
for i in range(1000, 10001):
    inicio = i // 100
    fim = i % 100
    if (inicio + fim) ** 2 == i:
        lista.append(i)
print(f'Os números verificados foram: {lista}')
