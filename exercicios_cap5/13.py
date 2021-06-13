"""
Questão 13
"""
NotaProva1 = float(input('Entre com a nota da prova1: '))
NotaProva2 = float(input('Entre com a nota da prova2: '))
NotaProva3 = float(input('Entre com a nota da prova3: '))

MediaPonderada = ((NotaProva1 + NotaProva2 + NotaProva3 * 2) / (1 + 1 + 3)) * 10
if MediaPonderada > 60:
    print(f'Aluno aprovado com média {MediaPonderada}.')
else:
    print(f'Aluno reprovado com média {MediaPonderada}.')
