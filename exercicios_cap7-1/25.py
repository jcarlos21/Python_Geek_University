"""
Questão 25
"""

vetor = []
valor = i = cont = 0
while i < 100:
    valor += 1
    if valor % 7 == 0 or valor % 10 == 7:
        vetor.append(valor)
        i += 1
        cont += 1
print(f'O vetor é: {vetor}')
