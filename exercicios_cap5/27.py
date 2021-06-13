"""
Questão 27
"""
Idade = int(input('Entre com uma idade acima de 5: '))
while Idade < 5:
    Idade = int(input('Muito nova! Entre com uma idade acima de 5: '))

if 5 <= Idade <= 7:
    print('Infantil A')
elif 8 <= Idade <= 10:
    print('Infantil B')
elif 11 <= Idade <= 13:
    print('Juvenil A')
elif 14 <= Idade <= 17:
    print('Juvenil B')
else:
    print('Sênior')

