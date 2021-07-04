"""
Questão 45
"""
print('PROGRAMA DE CONVERSÃO\n')
Opção = '1'
pergunta = 's'
velocidade = 0
while pergunta == 's':
    Opção = input('Digite uma das seguintes opções:\n'
                  '\n1 - km/h para m/s'
                  '\n2 - m/s para k/h'
                  '\n3 - sair do programa\n'
                  '\nOpção: ')

    while Opção != '1' and Opção != '2' and Opção != '3':  # Validação
        Opção = input('Dados inválidos! Por favor digite uma das seguintes opções:\n'
                      '\n1 - km/h para m/s'
                      '\n2 - m/s para k/h'
                      '\n3 - sair do programa\n'
                      '\nOpção: ')

    if Opção == '1':
        velocidade = float(input('Entre com uma velocidade em km/h para converter para m/s: '))
        print(f'\n{velocidade} equivale a {(velocidade / 3.6).__round__(2)} m/s')
    elif Opção == '2':
        velocidade = float(input('Entre com uma velocidade em m/s para converter para km/h: '))
        print(f'\n{velocidade} equivale a {(velocidade * 3.6).__round__(2)} km/h')

    if Opção == '3':
        pergunta = input('Realmente tem interesse em sair (s/n)? ')
        while pergunta != 's' and pergunta != 'n':
            pergunta = input('Dados inválidos! Digite s ou n: ')
        if pergunta == 's':
            pergunta = 'n'
        else:
            pergunta = 's'
    else:
        pergunta = input('Tem interesse em continuar (s/n)? ')
        while pergunta != 's' and pergunta != 'n':
            pergunta = input('Dados inválidos! Digite s ou n: ')
