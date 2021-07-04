"""
Questão 21
"""
num1 = int(input('Entre com um número inteiro: '))
num2 = int(input('Entre com outro número inteiro: '))
print()
soma = 0
mult = 1
if num1 < num2:
    for i in range(num1, num2+1):
        if i % 2 == 0:
            soma += i
        else:
            mult *= i
else:
    for i in range(num2, num1+1):
        if i % 2 == 0:
            soma += i
        else:
            mult *= i

if num1 < num2:
    print(f'A soma dos números pares é no intervalo de {num1} a {num2} é: {soma}')
    print(f'A multiplicação dos números ímpares é no intervalo de {num1} a {num2} é: {mult}')
else:
    print(f'A soma dos números pares é no intervalo de {num2} a {num1} é: {soma}')
    print(f'A multiplicação dos números ímpares é no intervalo de {num2} a {num1} é: {mult}')
