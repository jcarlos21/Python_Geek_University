"""
Questão 21
"""
print('Escolha a opção:')
print('1 - Soma de 2 números.'
      '\n2 - Diferença entre 2 números (maior pelo menor).'
      '\n3 - Produto entre 2 números.'
      '\n4 - Divisão entre 2 números (o denominador não pode ser zero).')
opção = input('Opção: ')

while not opção.isdecimal() or int(opção) < 1 or int(opção) > 4:
    print('\nOpção inválida!!!! Escolha uma das opções abaixo:')
    print('1 - Soma de 2 números.'
          '\n2 - Diferença entre 2 números (maior pelo menor).'
          '\n3 - Produto entre 2 números.'
          '\n4 - Divisão entre 2 números (o denominador não pode ser zero).')
    opção = input('Opção: ')
operação = int(opção)

print('\nAgora entre com 2 número para efetuar a operação')
num1 = input('\nNúmero 1: ')
num2 = input('Número 2: ')

cont = 2
while (not num1.isdigit() or not num2.isdigit()) and not cont == 0:
    if cont == 2:
        print(
            f'\nTá de brincadeira, é? Digite um número real pow! Se digitar errado mais {cont} vezes eu me encerro automaticamente!')
    else:
        print('\nExiste tempo pra tudo, inclusive pra isso! Digita certo dessa vez ou encerro o programa.')
    num1 = input('\nNuméro 1: ')
    num2 = input('Número 2: ')
    cont -= 1
    if cont == 0 and (not num1.isdigit() or not num2.isdigit()):
        print('\nEu avisei seu cabeção!!!!')

if int(operação) == 1:
    print(f'O resultado é: {float(num1) + float(num2)}')
elif int(operação) == 2:
    if num1 > num2:
        print(f'O resultado é: {float(num1) - float(num2)}')
    else:
        print(f'O resultado é: {float(num2) - float(num1)}')
elif int(operação) == 3:
    print(f'O resultado é: {float(num1) * float(num2)}')
else:
    if num2 != 0:
        print(f'O resultado é: {float(num1) / float(num2)}')
    else:
        print(f'O resultado é: {float(num2) / float(num1)}')
