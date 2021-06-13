"""
Questão 23
"""
ano = input('Entre com o ano: ')
while not ano.isdecimal():
    print('Ops! Valor inválido! Digite novamente!')
    ano = input('Ano: ')

Ano = int(ano)
if Ano % 400 == 0:
    print(f'O ano {Ano} é bisexto!')
elif Ano % 4 == 0 and not Ano % 100 == 0:
    print(f'O ano {Ano} é bisexto!')
else:
    print(f'O ano {Ano} não é bisexto!')
