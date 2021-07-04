"""
Questão 40
"""
num = 0
menor = 0
maior = i = 0
while num >= 0:
    num = int(input(f'Entre com o {i+1}° número: '))
    if i == 0:
        menor = num
        maior = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    i += 1
print(f'O menor número é {menor} e o maior é {maior}.')
