"""
Questão 14
"""
NotaTL = float(input('Entre com a nota do trabalho de laboratório: '))
NotaAvS = float(input('Entre com a nota da avaliação semestral: '))
NotaExFinal = float(input('Entre com a nota do exame final: '))

while (NotaTL < 0 or NotaTL > 10) or (NotaAvS < 0 or NotaAvS > 10) or (NotaExFinal < 0 or NotaExFinal > 10):
    print('Valores digitados inválidos. Por favor digite valores entre 0 e 10.')
    NotaTL = float(input('Entre com a nota do trabalho de laboratório: '))
    NotaAvS = float(input('Entre com a nota da avaliação semestral: '))
    NotaExFinal = float(input('Entre com a nota do exame final: '))

# Trabalho de laboratório - Peso 2
# Avaliação semestral - Peso 3
# Exame final - Peso 5

MediaPonderada = ((NotaTL * 2) + (NotaAvS * 3) + (NotaExFinal * 5)) / (2 + 3 + 5)
if 0 <= MediaPonderada <= 2.9:
    print('\nAluno reprovado.')
elif 3 <= MediaPonderada <= 4.9:
    print('\nAluno em recuperação.')
else:
    print('\nAluno aprovado. Parabens!!!')

print(f'\nMédia ponderada do aluno: {MediaPonderada}')
