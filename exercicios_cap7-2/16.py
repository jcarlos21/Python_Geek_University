"""
Questão 16
"""
"""
Alunos:
    Aluno 01:
        - matrícula; // inteiro
        - Respostas; // lista
        - Nota; // inteiro
        - Situação; //string
"""
aluno01 = {'Matrícula': 0000, 'Respostas': [], 'Nota': 0, 'Situação': ''}
aluno02 = {'Matrícula': 0000, 'Respostas': [], 'Nota': 0, 'Situação': ''}
aluno03 = {'Matrícula': 0000, 'Respostas': [], 'Nota': 0, 'Situação': ''}

resp = ['', '', '', '', '', '', '', '', '', '']
lista = [aluno01, aluno02, aluno03]
gabarito = ['d', 'b', 'a', 'e', 'c', 'b', 'e', 'a', 'd', 'c']

for i in range(0, len(lista)):
    lista[i]['Matrícula'] = int(input(f'Entre com a Matrícula (4 dígitos) para o {i+1}° aluno: '))
    for j in range(0, len(resp)):
        resp[j] = input(f'Digite a resposta da questão {j + 1}: ')
        while resp[j] != 'a' and resp[j] != 'b' and resp[j] != 'c' and resp[j] != 'd' and resp[j] != 'e':
            resp[j] = input(f'Resposta inválida! Digite novamente a resposta da questão {j + 1}: ')
    lista[i]['Respostas'] = resp.copy()  # meio usado para não cair no Shallow Copy
    print()

# comparação com o gabarito e obtenção da nota
cont = 0
for i in range(0, len(lista)):
    cont = 0
    for j in range(0, len(gabarito)):
        if lista[i]['Respostas'][j] == gabarito[j]:
            cont += 1
    lista[i]['Nota'] = cont
    if lista[i]['Nota'] >= 7:
        lista[i]['Situação'] = 'aprovado'
    else:
        lista[i]['Situação'] = 'reprovado'

# impressão dos dados
for i in range(0, len(lista)):
    for j, valor in lista[i].items():
        print(f'{j}: {valor}')
    print()
