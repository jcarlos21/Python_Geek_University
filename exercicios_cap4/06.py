"""
Questão 06
"""
celsius = float(input("Entre com uma temperatura em Celsius para converter para Fahrenheit: "))
print(f'{celsius}°C é igual a {(celsius * (9.0 / 5.0) + 32).__round__(2)}°F.')
