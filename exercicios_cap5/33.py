"""
Questão 33
"""
Preco = float(input('Entre com o preço do produto: '))
PrecoNovo = 0.0
if Preco < 50:
    PrecoNovo = (Preco * 1.05).__round__(2)
elif 50 <= Preco <= 100:
    PrecoNovo = (Preco * 1.10).__round__(2)
else:
    PrecoNovo = (Preco * 1.15).__round__(2)

if PrecoNovo < 80:
    print(f'\nO preço novo é R$ {PrecoNovo} e é BARATO.')
elif 80 <= PrecoNovo <= 120:
    print(f'\nO preço novo é R$ {PrecoNovo} e é NORMAL.')
elif 120 < PrecoNovo <= 200:
    print(f'\nO preço novo é R$ {PrecoNovo} e é BARATO.')
else:
    print(f'\nO preço novo é R$ {PrecoNovo} e é MUITO CARO.')