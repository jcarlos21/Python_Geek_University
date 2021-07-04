"""
Questão 46
"""
import random
num = random.randint(0, 1000)
chute = 2000
cont = 0
while chute != num:
    chute = int(input('Chute o número sorteado: '))
    if chute > num:
        print(f'O chute é maior que número sorteado! Tente de novo! \n')
        cont += 1
    elif chute < num:
        print(f'O chute é menor que número sorteado! Tente de novo! \n')
        cont += 1
    else:
        cont += 1
        print(f'Parabéns!!! Você acertou chutando {cont} vezes! \n')
