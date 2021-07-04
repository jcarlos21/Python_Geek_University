"""
Questão 44
"""
num = int(input('Entre com um número: '))
num1 = 0
num2 = 1
fib = 0

while fib < num:
    if fib == 0:
        print(num1, end=' ')
        print(num2, end=' ')

    fib = num1 + num2
    print(fib, end=' ')
    num1 = num2
    num2 = fib
