"""
Questão 50
"""
AlturaChico = float(input('Entre com a altura do Chico: '))
AlturaZe = float(input('Entre com a altura do Zé: '))
Ano = 0

while AlturaZe < AlturaChico:
    AlturaChico = AlturaChico + 2
    AlturaZe = AlturaZe + 3
    Ano += 1

print(f'Levará {Ano} anos para que a altura do Zé se iguale ou ultrapasse a altura do Chico.')
