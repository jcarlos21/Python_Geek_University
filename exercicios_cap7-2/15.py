"""
Questão 15
"""
matriz = [['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'],
          ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'],
          ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']]

resposta = ''
print('Resposta dos alunos (a, b, c, ou d)\n')
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[0])):
        resposta = input(f'Entre com a resposta {j + 1}ª resposta do aluno {i + 1}: ')
        while resposta != 'a' and resposta != 'b' and resposta != 'c' and resposta != 'd':
            resposta = input(f'Valor inválido. Entre com uma resposta válida: ')
        matriz[i][j] = resposta

gabarito = ['a', 'b', 'c', 'b', 'd', 'a', 'c', 'a', 'd', 'b']
pontos = []
cont = 0

for i in range(0, len(matriz)):
    cont = 0
    for j in range(0, len(gabarito)):
        if matriz[i][j] == gabarito[j]:
            cont += 1
    pontos.append(cont)

for i in range(0,len(pontos)):
    print(f'O {i+1}° aluno fez {pontos[i]} pontos.')
