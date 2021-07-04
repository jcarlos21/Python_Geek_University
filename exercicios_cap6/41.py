"""
Questão 41
"""
print('CÁCULO DA RESISTÊNCIA EM PARALELO (TERMINA QUANDO UM DOS RESISTORES FOR IGUAL A ZERO).')
R1 = 1
R2 = 1
while R1 != 0 and R2 != 0:
    R1 = float(input('Entre com o valor do resistor R1: '))
    R2 = float(input('Entre com o valor do resistor R2: '))
    print(f'A resistência em paralelo é: {(R1 * R2) / (R1 + R2)}\n')
