"""
Questão 02
"""

data = input('Entre com a data separa por /: ')
data = data.split('/')


def datachange(x):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    for i in range(1, 13):
        if int(x[1]) == i:
            print(f'{int(x[0])} de {meses[i-1]} de {int(x[2])}.')


datachange(data)
