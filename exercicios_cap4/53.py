"""
Questão 53
"""
Comprimento = float(input('Entre com o comprimento do terrento: '))
Largura = float(input('Entre com a largura do terreno: '))
PreçoTela = float(input('Entre com o preço da tela por metro: '))
print(f'O custo para cercar o terrreno é de: R$ {((2 * Comprimento + 2 * Largura) * PreçoTela).__round__(2)}')
