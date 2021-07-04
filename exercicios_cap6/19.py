"""
Questão 19
"""
num = int(input('Entre com um número entre 100 e 999: '))
lista = []
while num > 0:
    print(num % 10)
    lista.append(num % 10)
    num = num // 10
print(lista[::-1])
