"""
Questão 16
"""
vetor = []
valor = 0

for i in range(0, 5):
    valor = float(input(f'Entre com {i+1}° valor real: '))
    vetor.append(valor)

codigo = '5'
while codigo != '0' and codigo != '1' and codigo != '2':
    codigo = input('Entre com as seguintes opções:'
                   '\n0 - Sair'
                   '\n1 - Mostrar vetor na ordem direta'
                   '\n2 - Mostrar vetor na ordem inversa'
                   '\nOpção: ')
    if codigo != '0' and codigo != '1' and codigo != '2':
        print('\nNuméro inválido. Tente novamente!\n')

if codigo == '1':
    print(f'\nVetor na ordem direta: {vetor}')
elif codigo == '2':
    print(f'\nO vetor na ordem inversa: {vetor[::-1]}')
else:
    print('\nSaindo do programa!')
