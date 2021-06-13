"""
Questão 38
"""


def VerificaAno(year):
    year = int(year)
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and not year % 100 == 0:
        return True
    else:
        return False


def VerificaData(day, month, year):
    if (1 <= month <= 12) and (1 <= day <= 31):
        if month == 2:
            if VerificaAno(year) and (1 <= day <= 29):
                return True
            elif not (VerificaAno(year)) and (1 <= day <= 28):
                return True
            else:
                return False
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if 1 <= day <= 30:
                return True
            else:
                return False
        else:
            if 1 <= day <= 31:
                return True
            else:
                return False
    else:
        return False


print('Entre com a sua data de nascimento: ')

dia = int(input('Entre com o dia: '))
mes = int(input('Entre com o mês: '))
ano = int(input('Entre com o ano: '))

if VerificaData(dia, mes, ano):
    print('Data válida!')
else:
    print('Data inválida!')
