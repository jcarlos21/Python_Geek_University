"""
Questão 40
"""
print('O custo diário do serviço do encanador é R$ 30,00 com 8% de imposto de renda.')
dia = int(input('Entre com o número de dias necessários para o serviço do encanador: '))
print(f'O valor a ser pago ao encanador é: R$ {dia * 30.00}')
print(f'Com o imposto de renda (IR) o valor fica: R$ {((100 - 8) / 100) * (dia * 30.00)}')
