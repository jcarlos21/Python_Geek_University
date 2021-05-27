"""
Questão 41
"""
print('Cálculo do salário de um funcionário.')
valorHora = float(input('Entre com o valor ganho por hora: '))
horaTrabalhadas = float(input('Entre com o número de horas trabalhadas no mês: '))
print('\nSerá adicionado 10% ao salário do funcionário.')
print(f'O salário do funcionário será igual a: R$ {(((10 / 100) + 1) * (valorHora * horaTrabalhadas)).__round__(3)}')
