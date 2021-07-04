"""
Questão 36
"""
soma1 = 0
for i in range(1, 101):
    soma1 = soma1 + (i ** 2)

soma2 = 0
for g in range(1, 101):
    soma2 = (soma2 + g)
soma2 = soma2 ** 2

print(f'A soma 1 deu {soma1} e a soma 2 deu {soma2}. A diferença é {soma2 - soma1}')
