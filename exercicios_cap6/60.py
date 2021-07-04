"""
Questão 61
"""
num = 1
soma = cont = MediaPares = SomaPar = ContPar = 0
Maior = -100000000
Menor = 100000000

while num != 0:
    num = int(input('Entre com um número inteiro: '))
    if num != 0:
        soma += num
        cont += 1
    if num > Maior:
        Maior = num
    if num < Menor and num != 0:
        Menor = num
    if num % 2 == 0 and num != 0:
        SomaPar += num
        ContPar += 1

print(f'\nSoma de números digitados: {soma}'
      f'\nQuantidade de número digitados: {cont}'
      f'\nMédia de números digitados: {soma / cont}'
      f'\nMaior número digitado: {Maior}'
      f'\nMenor número digitado: {Menor}'
      f'\nMédia dos números pares: {SomaPar / ContPar}')

