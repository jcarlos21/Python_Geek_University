"""
Questão 51
"""
salario = 2000.0
Ano = 1996
Aumento = 1.015

for i in range(1, 25):
    if Ano == 1996:
        salario *= Aumento
    else:
        Aumento *= 2
        salario *= Aumento
print(f'O salário do funcionário em 2020 é: {salario.__round__(2)}')
