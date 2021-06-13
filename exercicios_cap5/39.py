""""
Questão 39
"""
SalarioAtual = float(input('Entre com o salário atual do funcionário: '))
TempodeServico = int(input('Entre com o tempo de serviço (em anos): '))

SalarioNovo = 0

if SalarioAtual <= 500 and TempodeServico < 1:
    SalarioNovo = SalarioAtual * 1.25
elif 500 < SalarioAtual <= 1000 and 1 <= TempodeServico <= 3:
    SalarioNovo = SalarioAtual * 1.20 + 100
elif 1000 < SalarioAtual <= 1500 and 4 <= TempodeServico <= 6:
    SalarioNovo = SalarioAtual * 1.15 + 200
elif 1500 < SalarioAtual <= 2000 and 7 <= TempodeServico <= 10:
    SalarioNovo = SalarioAtual * 1.10 + 300
else:
    SalarioNovo = SalarioAtual + 500

print(f'\nO novo salário do funcionário é: R$ {SalarioNovo}')

