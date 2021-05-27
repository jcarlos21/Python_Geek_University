"""
Questão 42
"""
salario = float(input('Entre com o valor do salário do funcionário: '))
print(f'O valor do novo salário é: R$ {((salario * ((5 / 100) + 1)) - (salario * (7 / 100))).__round__(2)}')
