""""
Questão 40
"""

CustoDeFabrica = float(input('Entre com o custo de fábrica: '))

if CustoDeFabrica <= 12000.0:
    print(f'O custo ao consumidor será de: R$ {CustoDeFabrica * 1.05}')
elif 12000.0 < CustoDeFabrica <= 25000.0:
    print(f'O custo ao consumidor será de: R$ {CustoDeFabrica + (CustoDeFabrica * 0.10) + (CustoDeFabrica * 0.15) }')
else:
    print(f'O custo ao consumidor será de: R$ {CustoDeFabrica + (CustoDeFabrica * 0.15) + (CustoDeFabrica * 0.20) }')

