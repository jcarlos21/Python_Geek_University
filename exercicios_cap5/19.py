"""
Questão 19
"""
num = input('Entre com um número inteiro: ')
print()
while num.isalpha() or not num.isdecimal():
    num = input('Sacangem! Digite o correto. Entre com um número inteiro: ')
    if not num.isalpha() or num.isdecimal():
        print()
# a função isdecimal() retorna True se o conteúdo da string é um inteiro ou não

if int(num) % 3 == 0 or int(num) % 5 == 0:
    if int(num) % 3 == 0 and int(num) % 5 == 0:
        print(f'O número {num} é divisível por 3 e 5.')
    elif int(num) % 3 == 0:
        print(f'O número {num} é divisível apenas por 3.')
    else:
        print(f'O número {num} é divisível por 5.')
else:
    print(f'O número {num} não é divisível por 3 nem por 5!')
