"""
Questão 49
"""
SalarioCarlos = float(input('Entre com o salário do Carlos: '))
SalarioJoao = SalarioCarlos / 3
NovoSalarioCarlos = SalarioCarlos
NovoSalarioJoao = SalarioJoao
Mes = 0

print('Vamos supor que tanto Carlos quanto João todos os meses coloquem seus salários nas aplicações.\n')

while NovoSalarioJoao < NovoSalarioCarlos:
    NovoSalarioCarlos = NovoSalarioCarlos * 1.02
    NovoSalarioJoao = NovoSalarioJoao * 1.05
    Mes += 1
    print(f'Rendimentos de Carlos: {NovoSalarioCarlos.__round__(2)}')
    print(f'Rendimentos de João: {NovoSalarioJoao.__round__(2)}')

print(f'Levará {Mes} meses para que o salário de João se iguale ou ultrapasse o salário de Carlos.')
