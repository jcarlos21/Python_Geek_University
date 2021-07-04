"""
Questão 62
"""


def QuantidadeLetras(x):
    modulo = x
    resto = 200  # Possui este valor para entrar no laço no while
    cont = 0

    unidade = ' '
    dezena = ' '  # lembre-se de trocar esses valores, caso a dezena seja zero, vc poderá fazer isso pondo uma condição na impressão
    centena = ' '
    milhares = ' '

    while resto >= 1:
        resto = modulo % 10
        modulo //= 10
        cont += 1
        # Bloco de comandos para unidades________________________________________________________________________
        if cont == 1:
            if resto == 1:
                unidade = 'um'
            elif resto == 2:
                unidade = 'dois'
            elif resto == 3:
                unidade = 'três'
            elif resto == 4:
                unidade = 'quatro'
            elif resto == 5:
                unidade = 'cinco'
            elif resto == 6:
                unidade = 'seis'
            elif resto == 7:
                unidade = 'sete'
            elif resto == 8:
                unidade = 'oito'
            elif resto == 9:
                unidade = 'nove'
            else:
                unidade = 'zero'
            # continua (lembra de colocar um else para quando resto == 0, ou seja, unidade = 'zero'; isso serivirá para o if abaixo)

        # Bloco de comandos para dezenas_________________________________________________________________________
        if cont == 2:  # condição para ser dezena
            if resto == 1:
                if unidade == 'zero':
                    dezena = 'dez'
                    unidade = ' '  # correção para que o caso que temos o número 10, 11, 12, ... , 19.
                elif unidade == 'um':
                    dezena = 'onze'
                    unidade = ' '
                elif unidade == 'dois':
                    dezena = 'doze'
                    unidade = ' '
                elif unidade == 'três':
                    dezena = 'treze'
                    unidade = ' '
                elif unidade == 'quatro':
                    dezena = 'catorze'
                    unidade = ' '
                elif unidade == 'cinco':
                    dezena = 'quinze'
                    unidade = ' '
                elif unidade == 'seis':
                    dezena = 'dezesseis'
                    unidade = ' '
                elif unidade == 'sete':
                    dezena = 'dezessete'
                    unidade = ' '
                elif unidade == 'oito':
                    dezena = 'dezoito'
                    unidade = ' '
                elif unidade == 'nove':
                    dezena = 'dezenove'
                    unidade = ' '
            elif resto == 2:
                if unidade == 'zero':
                    dezena = 'vinte'
                    unidade = ' '
                else:
                    dezena = 'vinte e '
            elif resto == 3:
                if unidade == 'zero':
                    dezena = 'trinta'
                    unidade = ' '
                else:
                    dezena = 'trinta e '
            elif resto == 4:
                if unidade == 'zero':
                    dezena = 'quarenta'
                    unidade = ' '
                else:
                    dezena = 'quarenta e '
            elif resto == 5:
                if unidade == 'zero':
                    dezena = 'cinquenta'
                    unidade = ' '
                else:
                    dezena = 'cinquenta e '
            elif resto == 6:
                if unidade == 'zero':
                    dezena = 'sessenta'
                    unidade = ' '
                else:
                    dezena = 'sessenta e '
            elif resto == 7:
                if unidade == 'zero':
                    dezena = 'setenta'
                    unidade = ' '
                else:
                    dezena = 'setenta e '
            elif resto == 8:
                if unidade == 'zero':
                    dezena = 'oitenta'
                    unidade = ' '
                else:
                    dezena = 'oitenta e '
            elif resto == 9:
                if unidade == 'zero':
                    dezena = 'noventa'
                    unidade = ' '
                else:
                    dezena = 'noventa e '
            else:  # Caso em que resto == 0 e cont == 2
                dezena = 'zero'  # Servirá para o if abaixo

        # Bloco de comandos para centenas________________________________________________________________________
        if cont == 3:  # condição para ser centena
            if resto == 1:
                if unidade == 'zero' and dezena == 'zero':
                    centena = 'cem'
                    unidade = ' '
                    dezena = ' '
                else:
                    centena = 'cento e '
            elif resto == 2:
                if unidade == 'zero' and dezena == 'zero':
                    centena = 'duzentos'
                    unidade = ' '
                    dezena = ' '
                else:
                    centena = 'duzentos e '
            elif resto == 3:
                if unidade == 'zero' and dezena == 'zero':
                    centena = 'trezentos'
                    unidade = ' '
                    dezena = ' '
                else:
                    centena = 'trezentos e '
            elif resto == 4:
                if unidade == 'zero' and dezena == 'zero':
                    centena = 'quatrocentos'
                    unidade = ' '
                    dezena = ' '
                else:
                    centena = 'quatrocentos e '
            elif resto == 5:
                if unidade == 'zero' and dezena == 'zero':
                    centena = 'quinhentos'
                    unidade = ' '
                    dezena = ' '
                else:
                    centena = 'quinhentos e '
            elif resto == 6:
                if unidade == 'zero' and dezena == 'zero':
                    centena = 'seiscentos'
                    unidade = ' '
                    dezena = ' '
                else:
                    centena = 'seiscentos e '
            elif resto == 7:
                if unidade == 'zero' and dezena == 'zero':
                    centena = 'setecentos'
                    unidade = ' '
                    dezena = ' '
                else:
                    centena = 'setecentos e '
            elif resto == 8:
                if unidade == 'zero' and dezena == 'zero':
                    centena = 'oitocentos'
                    unidade = ' '
                    dezena = ' '
                else:
                    centena = 'oitocentos e '
            elif resto == 9:
                if unidade == 'zero' and dezena == 'zero':
                    centena = 'novecentos'
                    unidade = ' '
                    dezena = ' '
                else:
                    centena = 'novecentos e '
            else:
                centena = 'zero'

        # Bloco de comandos para milhares________________________________________________________________________
        if resto != 0 and cont == 4:  # Não admite resto == 0
            if resto == 1:
                if unidade == 'zero' and dezena == 'zero' and centena == 'zero':
                    milhares = 'mil'
                    centena = ' '
                    dezena = ' '
                    unidade = ' '
                else:
                    if dezena == 'zero' and centena == 'zero':
                        milhares = 'mil e'
                    else:
                        milhares = 'mil'
            elif resto == 2:
                if unidade == 'zero' and dezena == 'zero' and centena == 'zero':
                    milhares = 'dois mil'
                    centena = ' '
                    dezena = ' '
                    unidade = ' '
                else:
                    if dezena == 'zero' and centena == 'zero':
                        milhares = 'dois mil e'
                    else:
                        milhares = 'dois mil'
            elif resto == 3:
                if unidade == 'zero' and dezena == 'zero' and centena == 'zero':
                    milhares = 'três mil'
                    centena = ' '
                    dezena = ' '
                    unidade = ' '
                else:
                    if dezena == 'zero' and centena == 'zero':
                        milhares = 'três mil e'
                    else:
                        milhares = 'três mil'
            elif resto == 4:
                if unidade == 'zero' and dezena == 'zero' and centena == 'zero':
                    milhares = 'quatro mil'
                    centena = ' '
                    dezena = ' '
                    unidade = ' '
                else:
                    if dezena == 'zero' and centena == 'zero':
                        milhares = 'quatro mil e'
                    else:
                        milhares = 'quatro mil'
            elif resto == 5:
                if unidade == 'zero' and dezena == 'zero' and centena == 'zero':
                    milhares = 'cinco mil'
                    centena = ' '
                    dezena = ' '
                    unidade = ' '
                else:
                    if dezena == 'zero' and centena == 'zero':
                        milhares = 'cinco mil e'
                    else:
                        milhares = 'cinco mil'
            elif resto == 6:
                if unidade == 'zero' and dezena == 'zero' and centena == 'zero':
                    milhares = 'seis mil'
                    centena = ' '
                    dezena = ' '
                    unidade = ' '
                else:
                    if dezena == 'zero' and centena == 'zero':
                        milhares = 'seis mil e'
                    else:
                        milhares = 'seis mil'
            elif resto == 7:
                if unidade == 'zero' and dezena == 'zero' and centena == 'zero':
                    milhares = 'sete mil'
                    centena = ' '
                    dezena = ' '
                    unidade = ' '
                else:
                    if dezena == 'zero' and centena == 'zero':
                        milhares = 'sete mil e'
                    else:
                        milhares = 'sete mil'
            elif resto == 8:
                if unidade == 'zero' and dezena == 'zero' and centena == 'zero':
                    milhares = 'oito mil'
                    centena = ' '
                    dezena = ' '
                    unidade = ' '
                else:
                    if dezena == 'zero' and centena == 'zero':
                        milhares = 'oito mil e'
                    else:
                        milhares = 'oito mil'
            elif resto == 9:
                if unidade == 'zero' and dezena == 'zero' and centena == 'zero':
                    milhares = 'nove mil'
                    centena = ' '
                    dezena = ' '
                    unidade = ' '
                else:
                    if dezena == 'zero' and centena == 'zero':
                        milhares = 'nove mil e'
                    else:
                        milhares = 'nove mil'

        if (cont == 1 or cont == 2 or cont == 3) and resto == 0:
            resto = 1
        if cont == 4:
            if dezena == 'zero':
                dezena = ''
            if centena == 'zero':
                centena = ''

        # print(f'O número {numero} por extenso é: {milhares} {centena}{dezena}{unidade}')

        # print(f'Quantidade de letras presente no número por extenso: {len(milhares) + len(centena) + len(dezena) + len(unidade)}')
    return len(milhares) + len(centena) + len(dezena) + len(unidade)


soma = 0
for i in range(1, 1000):
    soma = soma + QuantidadeLetras(i)

print(f'Do número 1 ao 1000 existe {soma} letras. ')

