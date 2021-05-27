"""
Questão 43
"""
valorProduto = float(input('Entre com o valor do produto: '))
print(f'O valor a ser pago a vista (com desconto de 10%) é: R$ {(valorProduto * (1 - (10 / 100))).__round__(2)}')
print(f'O valor a ser pago parcelado em 3x sem juros é: R$ {(valorProduto / 3).__round__(2)}')
print(f'Comissão do vendedor sob a compra a vista: R$ {((valorProduto * (1 - (10 / 100))) * (5 / 100)).__round__(2)}')
print(f'Comissão do vendedor sob a compra a vista: R$ {(valorProduto * (5 / 100)).__round__(2)}')
