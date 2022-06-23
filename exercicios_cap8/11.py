"""
Questão 11
"""


def nota_aluno(n1, n2, n3, letra):
    if letra == 'A':
        return (n1 + n2 + n3) / 3
    if letra == 'P':
        return (n1 * 5 + n2 * 3 + n3 * 2) / (5 + 3 + 2)


nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))
nota3 = float(input('Entre com a terceira nota: '))
letter = input('Entre com a letra A ou P para cálcula a media aritmética ou a média ponderada (pesos 5, 3 e 2): ')
print(f'A média das notas é: {(nota_aluno(nota1, nota2, nota3, letter)).__round__(2)}')
