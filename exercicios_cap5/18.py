"""
Questão 18
"""
print('Entre com uma das operações abaixo:')
print('\n Digite 1 para adição'
      '\n Digite 2 para subtração'
      '\n Digite 3 para multiplicação'
      '\n Digite 4 para divisão')
operação = input('\nEntre com um número para efetuar uma operação: ')

while not operação.isdigit() or float(operação) < 1 or float(operação) > 4 :
    print('\nO que foi digitado não corresponde a um número ou não está no intervalo de 1 a 4. Digite novamente uma das opções abaixo: '
          '\n Digite 1 para adição'
          '\n Digite 2 para subtração'
          '\n Digite 3 para multiplicação'
          '\n Digite 4 para divisão')
    operação = input('\n Qual opção: ')

print('\nAgora entre com 2 número para efetuar a operação')
num1 = input('\nNúmero 1: ')
num2 = input('Número 2: ')

cont = 2
while (not num1.isdigit() or not num2.isdigit()) and not cont == 0:
    if cont == 2:
        print(f'\nTá de brincadeira, é? Digite um número real pow! Se digitar errado mais {cont} vezes eu me encerro automaticamente!')
    else:
        print('\nExiste tempo pra tudo, inclusive pra isso! Digita certo dessa vez ou encerro o programa.')
    num1 = input('\nNuméro 1: ')
    num2 = input('Número 2: ')
    cont -= 1
    if cont == 0 and (not num1.isdigit() or not num2.isdigit()):
        print('\nEu avisei seu cabeção!!!!')

print()
if int(operação) == 1:
    print(f'O resultado é: {float(num1) + float(num2) }')
elif int(operação) == 2:
    print(f'O resultado é: {float(num1) - float(num2) }')
elif int(operação) == 3:
    print(f'O resultado é: {float(num1) * float(num2) }')
else:
    print(f'O resultado é: {float(num1) / float(num2) }')
