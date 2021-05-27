"""
Questão 52
"""
apostador1 = float(input('Entre com o valor da primeira aposta: '))
apostador2 = float(input('Entre com o valor da segunda aposta: '))
apostador3 = float(input('Entre com o valor da terceira aposta: '))

Total = apostador1 + apostador2 + apostador3

premio = float(input('Entre com o valor do premio: '))
print(f'O primeiro apostador receberá: R$ {((apostador1 / Total) * premio).__round__(2)}')
print(f'O segundo apostador receberá: R$ {((apostador2 / Total) * premio).__round__(2)}')
print(f'O terceiro apostador receberá: R$ {((apostador3 / Total) * premio).__round__(2)}')
