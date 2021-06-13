"""
Questão 28
"""
x = int(input('Entre com um número inteiro: '))
y = int(input('Entre com um número inteiro: '))
z = int(input('Entre com um número inteiro: '))

operação: int = int(input('\nEntre com uma das médias abaixo:'
                     '\n1 - Geométrica'
                     '\n2 - Ponderada'
                     '\n3 - Harmônica'
                     '\n4 - Aritmética'
                     '\nOpção: '))
while not 1 <= operação <= 4:
    operação = int(input('\nValor inválido! Entre com uma das médias abaixo:'
                         '\n1 - Geométrica'
                         '\n2 - Ponderada'
                         '\n3 - Harmônica'
                         '\n4 - Aritmética'
                         '\nOpção: '))

if operação == 1:
    print(f'A média geométrica é: {(x * y * z) ** (1 / 3)}')
elif operação == 2:
    print(f'A média ponderada é: {(x + 2 * y + 3 * z) / 6}')
elif operação == 3:
    print(f'A média harmônica é: {1 / ((1 / x) + (1 / y) + (1 / z))}')
else:
    print(f'A média aritmética é: {(x + y + z) / 3}')



