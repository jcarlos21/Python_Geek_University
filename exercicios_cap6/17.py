"""
Questão 16
"""
N = int(input('Entre com um número inteiro: '))
soma = 0
for i in range(1, N+1):
    soma += i
print(f'A soma dos {N} primeiros números naturais é: {soma} ')
