"""
Questão 68
"""


def IntercalaStrings(str1, str2):
    str3 = ''
    if len(str1) == len(str2):
        for a in range(0, len(str1)):
            str3 = str3 + str1[a] + str2[a]  # está somando a str3 para concatenar com os próximos caracteres
    else:
        return 'Os tamnhos devem ser iguais!'
    str1 = str3
    return str1


string01 = input('Entre com palavra ou frase: ')
string02 = input('Entre com outra palavra ou outra frase para comparar: ')
print(f'Os textos ou palavras inseridos intercalados ficam: {IntercalaStrings(string01, string02)}')
