"""
Questão 30
"""
x = float(input('Entre com um número inteiro: '))
y = float(input('Entre com um número inteiro: '))
z = float(input('Entre com um número inteiro: '))

if z > y > x < y:  # Se x menor que y e z; e y menor que z
    print(f'{x, y, z}')
elif x < y and x < z < y:  # Se x menor que y e z; e y maior que z
    print(f'{x, z, y}')
elif z > x > y < x:  # Se y menor que x e z; e x menor que z
    print(f'{y, x, z}')
elif y < x and y < z < x:  # Se y menor que x e z; e x maior que z
    print(f'{y, z, x}')
elif x > y > z < y:  # Se z menor que y e x; e y menor que x
    print(f'{z, y, x}')
else:  # Se z menor que y e x; e y maior que x
    print(f'{z, x, y}')

# z < y and z < x < y
