"""
Questão 10
"""
vetor = []
valor = 0
print('Entre com as notas dos 15 alunos:')
for i in range(0, 15):
    valor = float(input(f'Entre com {i+1}ª nota: '))
    vetor.append(valor)

print(f'A média das notas é: {(sum(vetor) / len(vetor)).__round__(2)}.')
