"""
Questão 08
"""
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
if (0.0 <= nota1 <= 10.0) and (0.0 <= nota2 <= 10.0):
    print(f'A média das notas digitas é: {((nota1 + nota2) / 2).__round__(2)}.')
else:
    print('As notas digitadas não são válidas.')
