"""
Questão 24
"""
P = float(input('Entre com o valor do produto: '))
Estado = input('Entre com um dos estados a seguir:'
               '\nMG - Mato Grosso - 7%'
               '\nSP - São Paulo - 12%'
               '\nRJ - Rio de Janeiro - 15%'
               '\nMS - Mato Grosso do Sul - 8%'
               '\nOpção: ')
while not Estado == 'MG' and not Estado == 'SP' and not Estado == 'RJ' and not Estado == 'MS':
    Estado = input('Valor inválido!'
                   '\nEntre com um dos estados a seguir:'
                   '\nMG - Mato Grosso - 7%'
                   '\nSP - São Paulo - 12%'
                   '\nRJ - Rio de Janeiro - 15%'
                   '\nMS - Mato Grosso do Sul - 8%'
                   '\nOpção: ')

if Estado == 'MG':
    print(f'No estado {Estado} o produto será vendido ao preço de {P * 1.07}')
elif Estado == 'SP':
    print(f'No estado {Estado} o produto será vendido ao preço de {P * 1.12}')
elif Estado == 'RJ':
    print(f'No estado {Estado} o produto será vendido ao preço de {P * 1.15}')
else:
    print(f'No estado {Estado} o produto será vendido ao preço de {P * 1.08}')
