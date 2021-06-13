"""
Questão 06
"""
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
if num1 > num2:
    print(f'O primeiro número é maior que o segundo e a diferença entre eles é de {num1 - num2}.')
elif num1 == num2:
    print('Os número são iguais!')
else:
    print(f'O segundo número é maior que o primeiro e a diferença entre eles é de {num2 - num1}.')
