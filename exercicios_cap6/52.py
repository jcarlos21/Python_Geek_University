"""
Questão 52
"""
saque = float(input('Entre com o valor do saque: '))
resto1 = resto2 = resto3 = resto4 = 0
a = b = c = d = e = 0
MenorNumNotas = 10000000000000000
MenorResto = 1000000000000000
MenorRestoResto = 1000000000000
MenorRestoU = 100000000000
MenorRestoW = 1000000000

for i in range(1, 101):
    if i == 1 or i == 2 or i == 5 or i == 10 or i == 20 or i == 50 or i == 100:
        if saque // i < MenorNumNotas and saque // i != 0:
            MenorNumNotas = saque // i
            resto1 = saque % i
            a = i

for g in range(1, 51):
    if g == 1 or g == 2 or g == 5 or g == 10 or g == 20 or g == 50:
        if resto1 // g < MenorResto and resto1 // g != 0:
            MenorResto = resto1 // g
            resto2 = resto1 % g
            b = g
        else:
            if g == 1:
                MenorResto = 0

for j in range(1, 11):
    if j == 1 or j == 2 or j == 5 or j == 10:
        if resto2 // j < MenorRestoResto and resto2 // j != 0:
            MenorRestoResto = resto2 // j
            resto3 = resto2 % j
            c = j
        else:
            if j == 1:
                MenorRestoResto = 0

for h in range(1, 3):
    if h == 1 or h == 2:
        if resto3 // h < MenorRestoU and resto3 // h != 0:
            MenorRestoU = resto3 // h
            resto4 = resto3 % h
            d = h
        else:
            if h == 1:
                MenorRestoU = 0

for m in range(1, 3):
    if m == 1 or m == 2:
        if resto4 // m < MenorRestoW and resto4 // m != 0:
            MenorRestoW = resto4 // m
            e = m
        else:
            if m == 1:
                MenorRestoW = 0

print(f'Quantidade de notas: {MenorNumNotas} notas de {a} reais, {MenorResto} notas de {b} reais,'
      f'\n{MenorRestoResto} notas de {c} reais, {MenorRestoU} notas de {d} reais, {MenorRestoW} notas de {e} reais.')
print(f'Total de notas: {MenorNumNotas + MenorResto + MenorRestoResto + MenorRestoU + MenorRestoW}')

# Se desejar pode modificar a impressão para que não apareça a situação de ter "0 notas de 0 reais"
