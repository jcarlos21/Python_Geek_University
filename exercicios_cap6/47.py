"""
Questão 47
"""
Operação = '1'
num1 = 0
num2 = 0
resultado = 0

while Operação != '5':
    Operação = input('Entre com uma das oprações abaixo:\n'
                     '\n1 - Adição'
                     '\n2 - Subtração'
                     '\n3 - Multiplicação'
                     '\n4 - Divisão'
                     '\n5 - Para sair do programa\n'
                     '\nOpção: ')
    while Operação != '5' and Operação != '1' and Operação != '2' and Operação != '3' and Operação != '4':  # Validação da entrada da Operação
        Operação = input('\nDados inválidos! Entre com uma das opções:\n'
                         '\n1 - Adição'
                         '\n2 - Subtração'
                         '\n3 - Multiplicação'
                         '\n4 - Divisão'
                         '\n5 - Para sair do programa\n'
                         '\nOpção: ')

    if Operação == '1':
        num1 = float(input('\nEntre com um número para fazer a operação escolhida: '))
        num2 = float(input('Entre com um outro número para fazer a operação escolhida: '))
        resultado = num1 + num2
        print(f'O resultado é: {resultado}\n')
    elif Operação == '2':
        num1 = float(input('\nEntre com um número para fazer a operação escolhida: '))
        num2 = float(input('Entre com um outro número para fazer a operação escolhida: '))
        resultado = num1 - num2
        print(f'O resultado é: {resultado}\n')
    elif Operação == '3':
        num1 = float(input('\nEntre com um número para fazer a operação escolhida: '))
        num2 = float(input('Entre com um outro número para fazer a operação escolhida: '))
        resultado = num1 * num2
        print(f'O resultado é: {resultado}\n')
    elif Operação == '4':
        num1 = float(input('\nEntre com um número para fazer a operação escolhida: '))
        num2 = float(input('Entre com um outro número para fazer a operação escolhida: '))
        if num2 != 0:
            resultado = num1 / num2
            print(f'O resultado é: {resultado}\n')
        elif num1 != 0:
            resultado = num2 / num1
            print(f'O resultado é: {resultado}\n')
        else:
            print('Os dois valores não podem ser zero. O processo será reiniciado!')
    else:
        print('Saindo do programa! Bye!!!')
