"""
Questão 39
"""
valorConcurso = float(input('Entre com o valor do concurso: '))
print(f'O primeiro ganhador recebe 46% do prêmio: R$ {((46 / 100) * valorConcurso).__round__(2)}')
print(f'O segundo ganhador recebe 32% do prêmio: R$ {((32 / 100) * valorConcurso).__round__(2)}')
print(f'O segundo ganhador recebe o restante: R$ {((22 / 100) * valorConcurso).__round__(2)}')
