"""
Questão 36
"""

ValorVenda = float(input('Entre com o valor da venda: '))
Comissão = 0.0

if ValorVenda >= 100000.0:
    Comissão += 700.0 + ValorVenda * 0.16
elif 100000.0 > Comissão >= 80000.0:
    Comissão += 650.0 + ValorVenda * 0.14
elif 80000.0 > Comissão >= 60000.0:
    Comissão += 600.0 + ValorVenda * 0.14
elif 60000.0 > Comissão >= 40000.0:
    Comissão += 550.0 + ValorVenda * 0.14
elif 40000.0 > Comissão >= 20000.0:
    Comissão += 500.0 + ValorVenda * 0.14
else:
    Comissão += 400.0 + ValorVenda * 0.14

print(f'A comissão do vendedor é: R$ {Comissão}')
