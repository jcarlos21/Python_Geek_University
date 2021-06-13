"""
Questão 15
"""
num = input('Entre com um número inteiro de 1 a 7: ')
while not num.isdigit() or 0 <= int(num) > 7:
    num = input('O que foi digitado não corresponde a um número ou nã está no intervalo de 1 a 7. Digite novamente: ')

""" a condição de parada do loop while (not num.isdigit()) indica que
se num.isdigit() == False a expressão (not num.isdigit()) será True. Logo o loop irá continuar.
"""

if num.isdigit():
    num = int(num)
    if num == 1:
        print('É domingo.')
    elif num == 2:
        print('É segunda-feira.')
    elif num == 3:
        print('É terça-feira.')
    elif num == 4:
        print('É quarta-feira.')
    elif num == 5:
        print('É quinta-feira.')
    elif num == 6:
        print('É sexta-feira.')
    else:
        print('É sábado.')
