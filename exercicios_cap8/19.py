"""
Questão 19
"""


def eh_primo(x):
    cont = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cont += 1
    if cont == 2:
        return True
    return False


def maiorprimo(x):
    i = 2
    maior = 0
    lista = []
    while x != 1:
        if eh_primo(i):
            if x % i == 0:
                maior = i
                x = (x / i)
                lista.append(i)
                # lista para guardar os fatores primos ?
                while x % i == 0:
                    x = (x / i)
                    lista.append(i)
        i += 1
        if x == 1:
            return maior, lista


num = int(input('Entre com um número inteiro: '))
fator, lista_de_fatores = maiorprimo(num)

print(f'\nO maior fator primo de {num} é: {fator}'
      f'\nA lista de fatores é: {lista_de_fatores}')
