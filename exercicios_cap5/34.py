"""
Questão 34
"""
Nota = float(input('Entre com a nota: '))
Faltas = int(input('Entre com o número de faltas: '))

if Faltas <= 20:
    if 0.0 <= Nota <= 3.9:
        print(f'Aluno com conceito E')
    elif 4.0 <= Nota <= 4.9:
        print(f'Aluno com conceito D')
    elif 5.0 <= Nota <= 7.4:
        print(f'Aluno com conceito C')
    elif 7.5 <= Nota <= 8.9:
        print(f'Aluno com conceito B')
    else:
        if 9.0 <= Nota <= 10.0:
            print(f'Aluno com conceito A')
        else:
            print('Nota inválida')
else:  # Mais de 20 faltas
    if 0.0 <= Nota <= 3.9:
        print(f'Aluno com conceito E')
    elif 4.0 <= Nota <= 4.9:
        print(f'Aluno com conceito E')
    elif 5.0 <= Nota <= 7.4:
        print(f'Aluno com conceito D')
    elif 7.5 <= Nota <= 8.9:
        print(f'Aluno com conceito C')
    else:
        if 9.0 <= Nota <= 10.0:
            print(f'Aluno com conceito B')
        else:
            print('Nota inválida')