"""
Questão 06
"""


def segundos(hora, minuto, segundo):
    return (hora * 3600) + (minuto * 60) + segundo


hours = input('Entre com a hora: ')
minutes = input('Entre com os munutos: ')
seconds = input('Entre com os segundos: ')

print(f'São {segundos(int(hours), int(minutes), int(seconds))} segundos.')
