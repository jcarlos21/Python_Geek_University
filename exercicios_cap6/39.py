"""
Questão 39
"""
Base = int(input('Entre com uma base diferente de zero: '))
Altura = int(input('Entre com uma altura dirferente de zero: '))

while Base <= 0 or Altura <= 0:
    print('Dados inválidos! Por favor digite-os novamente.')
    Base = int(input('Base: '))
    Altura = int(input('Altura: '))

AreaTriangulo = (Base * Altura) / 2

print(f'A área do triângulo é: {AreaTriangulo}')
