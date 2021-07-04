"""
Questão 57
"""
a = int(input('Entre com um número inteiro: '))
b = int(input('Entre com um número inteiro: '))
ContVerificaPrimo = 0
ContadorPrimo = 0

for i in range(a, b + 1):  # Vezes que o laço vai rodar
    ContVerificaPrimo = 0
    for j in range(1, i + 1):  # Laço responsável pela verificação de cada número do intervalo (a, b)
        if i % j == 0:
            ContVerificaPrimo += 1
    if ContVerificaPrimo == 2 or ContVerificaPrimo == 1:
        ContadorPrimo += 1

print(f'Entre {a} e {b} há {ContadorPrimo} números primos.')
