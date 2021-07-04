"""
Questão 22
"""
nota = 15
soma = 0
cont = 0
while 10 <= nota <= 20:
    nota = float(input('Insira uma nota (terminar quando a nota não estiver entre  10 e 20): '))
    if 10 <= nota <= 20:
        soma += nota
        cont += 1

print(f'A média aritmética das notas digitadas é: {soma / cont}')
