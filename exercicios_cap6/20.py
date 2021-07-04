"""
Questão 20
"""
num = cont = i = 0
while num != 1000:
    num = int(input(f'Entre com o {i+1}° número (termina quando for digitado 1000): '))
    if num % 2 == 0:
        print(f'O número {num} é par. ')
        cont += 1
    else:
        print(f'O número {num} não é par. ')
    i += 1

print(f'Houve {cont} números pares.')
