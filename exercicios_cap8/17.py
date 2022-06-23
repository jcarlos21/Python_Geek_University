"""
Questão 17
"""


def SomaEntreNumeros(num1, num2):
    soma = 0
    for i in range(num1 + 1, num2):
        soma += i
    return soma


numero1 = int(input('Entre com um número inteiro positivo: '))
numero2 = int(input('Entre com um número inteiro positivo maior que o anterior: '))

print(f'A soma dos números existente entre {numero1} e {numero2} é: {SomaEntreNumeros(numero1, numero2)}')

