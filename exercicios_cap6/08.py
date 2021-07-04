"""
Questão 08
"""
num = 0
menor = 0
maior = 0
for i in range(0, 10):
    num = int(input(f'Entre com o {i+1}° número: '))
    if i == 0:
        menor = num
        maior = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print(f'O menor número é {menor} e o maior é {maior}.')
