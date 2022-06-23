"""
Questão 27
"""


def serie(N):
    S = 0
    for i in range(1, N+1):
        S = S + (i**2 + 1)/(i + 3)
    return S


num = int(input("Entre com um número inteiro: "))
print(f'O valor da série é: {serie(num)}')
