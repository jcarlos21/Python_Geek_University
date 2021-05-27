"""
Questão 48
"""
segundos = int(input('Entre com um valor em segundos: '))
# print(f'O valor digitado equivale a {}')

print(f'O valor digitado equivale a {segundos // 3600} horas, {(segundos % 3600) // 60} minutos e {(segundos % 3600) % 60} segundos.')

