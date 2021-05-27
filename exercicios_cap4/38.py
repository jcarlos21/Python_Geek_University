"""
Questão 38
"""
salarioAtual = float(input('Entre com o valor do salário do funcionário: '))
aumento = float(input('Entre com o valor do aumento: '))
print(f'O valor do novo salário é: R$ {(salarioAtual * ((aumento / 100) + 1)).__round__(2)}')
