"""
Questão 15
"""
import math

R = float(input("Entre com um ângulo em radianos para converter para graus: "))
print(f'{R} rad é igual a {(R * (180 / math.pi)).__round__(2)}°.')
