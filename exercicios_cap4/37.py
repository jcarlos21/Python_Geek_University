"""
Questão 37
"""
valorProduto = float(input('Entre com o valor do produto: '))
save = float(input('Entre com o valor do desconto: '))
print(f'O valor do produto com o desconto é: R$ {(valorProduto * ((100.0 - save) / 100.0)).__round__(2)}')
