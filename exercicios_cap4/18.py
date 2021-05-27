"""
Questão 18
"""

M = float(input("Entre com um volume em metros cúbicos para converter para litros: "))
print(f'{M} m³ é igual a {(int(1000 * M)).__round__(2)} litros.')
