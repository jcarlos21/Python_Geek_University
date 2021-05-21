"""
Questão 07
"""
F = float(input("Entre com uma temperatura em Fahrenheit para converter para Celsius: "))
print(f'{F}°F é igual a {((F - 32) * (5.0 / 9.0)).__round__(4)}°C.')

