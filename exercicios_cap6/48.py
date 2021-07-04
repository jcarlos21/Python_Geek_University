"""
Questão 48
"""
num1 = 0
num2 = 1
fib = 0
soma = 0

while soma < 4000000:
    if fib == 0:
        print(num1, end=' ')
        print(num2, end=' ')

    fib = num1 + num2
    if fib % 2 == 0:
        soma += fib
    print(fib, end=' ')
    num1 = num2
    num2 = fib

print(f'\nA soma dos números pares da sequência de Fibonacci é: {soma}')
