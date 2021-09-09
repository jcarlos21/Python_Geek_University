"""
Questão 24
"""
Aluno = []
Altura = []
CodigoAluno = 0
ValorAltura = 0.0

for i in range(0, 10):
    CodigoAluno = int(input(f'Entre com o código do {i+1}° aluno: '))
    Aluno.append(CodigoAluno)
    ValorAltura = float(input(f'Entre com o valor da altura do {i+1}° aluno: '))
    Altura.append(ValorAltura)

menor = maior = Altura[0]
indiceMenor = 0
indiceMaior = 0
for j in range(0, 10):
    if Altura[j] < menor:
        menor = Altura[j]
        indiceMenor = j
    if Altura[j] > maior:
        maior = Altura[j]
        indiceMaior = j

print(f'\nA menor e maior altura são:'
      f'\nMenor altura: {menor}; Aluno: {Aluno[indiceMenor]}'
      f'\nMaior altura: {maior}; Aluno: {Aluno[indiceMaior]}')
