"""
Questão 22
"""
Idade = input('Entre com a idade: ')
TempoServico = input('Entre com o tempo de srviço (em anos): ')

while not Idade.isdecimal() or not TempoServico.isdecimal():
    print('Dados inválidos! Por favor faça conforme pedido: ')
    Idade = input('Entre com a idade: ')
    TempoServico = input('Entre com o tempo de serviço (em anos): ')

if int(Idade) >= 60:
    print('O trabalhador pode se aposentar!')
elif int(TempoServico) >= 30:
    print('O trabalhador pode se aposentar!')
elif int(Idade) >= 60 and int(TempoServico) >= 25:
    print('O trabalhador pode se aposentar!')
else:
    print('O trabalhador não pode se aposentar!')
