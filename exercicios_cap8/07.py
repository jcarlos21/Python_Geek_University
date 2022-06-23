"""
Questão 07
"""


def fahrenheit(celsius):
    return celsius * (9.0 / 5.0) + 32.0


temperatura = float(input('Entre com uma temperatura em graus celsius: '))
print(f'A temperatura {temperatura}°C equivale a {(fahrenheit(temperatura)).__round__(2)}°F.')
