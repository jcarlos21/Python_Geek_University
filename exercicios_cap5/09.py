"""
Questão 09
"""
Salario = float(input('Entre com o salário do funcionário: '))
Emprestimo = float(input('Entre com o valor da parcela do emprestimo: '))
if (Emprestimo / Salario) > 0.20:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')
