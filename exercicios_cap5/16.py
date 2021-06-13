"""
Questão 16
"""
num = input('Entre com um número inteiro de 1 a 12: ')
while not num.isdigit() or int(num) > 12 or int(num) < 1:
    num = input('O que foi digitado não corresponde a um número ou nã está no intervalo de 1 a 12. Digite novamente: ')

""" a condição de parada do loop while (not num.isdigit()) indica que
se num.isdigit() == False a expressão (not num.isdigit()) será True. Logo o loop irá continuar.
"""

if num.isdigit():
    num = int(num)
    if num == 1:
        print('É janeiro.')
    elif num == 2:
        print('É fevereiro.')
    elif num == 3:
        print('É março.')
    elif num == 4:
        print('É abril.')
    elif num == 5:
        print('É maio.')
    elif num == 6:
        print('É junho.')
    elif num == 7:
        print('É julho.')
    elif num == 8:
        print('É agosto.')
    elif num == 9:
        print('É setembro.')
    elif num == 10:
        print('É outubro.')
    elif num == 11:
        print('É novembro.')
    else:
        print('É dezembro.')
