"""
Questão 61
"""
respostaInteira = 0
respostaString = '55'
RespostaFinal = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        respostaInteira = i * j
        respostaString = str(respostaInteira)
        if respostaString == respostaString[::-1]:
            RespostaFinal = respostaInteira
            break
    if respostaString == respostaString[::-1]:
        RespostaFinal = respostaInteira
        break

print(f'O maior palíndromo de obtido por meio do produto de dois números de três dígitos eh: {i} * {j} = {RespostaFinal}')
