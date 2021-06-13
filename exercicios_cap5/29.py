"""
Questão 29
"""
from random import randint

i = 0
cont = 0
while i < 5:
    a = randint(0, 100)
    b = randint(0, 100)
    RespSistema = a + b
    RespAluno = int(input(f'Pergunta {i + 1} - Qual o resultado da soma ({a} + {b}) ?'
                    f'\nResposta: '))
    if RespAluno == RespSistema:
        print('Você acertou!!!\n')
        cont += 1
    else:
        print(f'Você errou! A resposta correta é: {a + b}\n')
    i += 1

print(f'Você acertou {cont} vezes.')
