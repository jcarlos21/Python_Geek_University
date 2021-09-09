"""
Questão 39
"""
Pascal = []
n = int(input('Entre com um número inteiro: '))
c = 1
p = 0
a = 1  # tem que ajeitar
b = 2  # tem que ajeitar depois de fazer o 2. kkkkkkkkk

for i in range(0, n):  # n é a quantidade de linhas de impressão
    for j in range(0, c):  # esse laço é responsável pela forma do triângulo, imprime cada elemento na mesma linha por meior do print(Pascal[j], end=' ')
        if 1 <= j < (c - 1) and c >= 3 and i >= 2:
            Pascal.append(Pascal[a] + Pascal[b])
            a += 1
            b += 1
        if j == 0 or j == (c - 1):  # só adiciono 1 quando estiver no começo ou no fim do vetor
            Pascal.append(1)
        print(Pascal[p], end=' ')
        p += 1
    if i >= 2:
        a += 1
        b += 1
    c += 1
    print()
