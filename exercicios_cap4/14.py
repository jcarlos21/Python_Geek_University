"""
Questão 14
"""
import math

G = float(input("Entre com um ângulo para converter para radianos: "))
print(f'{G}° é igual a {(G * math.pi / 180).__round__(2)} rad.')
