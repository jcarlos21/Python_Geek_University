"""
Questão 43
"""
idade = 2
soma = cont = 0
while idade > 0:
    idade = int(input('Entre com uma idade (termina quando for digitado um número menor ou igual a zero): '))
    soma += idade
    if idade > 0:
        cont += 1
print(f'A média das idades é: {soma / cont}')
print(f'O contador é: {cont}')
