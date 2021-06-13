"""
Questão 32
"""
print('Bem-vindo ao Ana Lanches! Confira a tabela de preços abaixo:\n')
print('Especificação     Código        Preço'
      '\nCachorro Quente    100         R$ 1.50'
      '\nBauru Simples      101         R$ 1.30'
      '\nBauru com Ovo      102         R$ 1.50'
      '\nHamburguer         103         R$ 1.20'
      '\nCheeseburguer      104         R$ 1.70'
      '\nSuco               105         R$ 2.20'
      '\nRefrigerante       106         R$ 1.00')


def VerificaCodigo():
    while True:
        x = input('\nCódigo do produto escolhido: ')
        if x.isnumeric() and (100 <= int(x) <= 106):  # dentro do úiltimo parenteses tem um "and"
            return int(x)
        else:
            print('Dados inválidos! Digite-os novamente!')
            continue


def VerificaQuantidade():
    while True:
        x = input('\nQuantidade: ')
        if x.isnumeric():
            return int(x)
        else:
            print('Dados inválidos! Digite-os novamente!')
            continue


i = 's'
conta = 0
codigo = '0'
Quantidade = '0'

while i != 'n':
    Codigo = VerificaCodigo()
    Quantidade = VerificaQuantidade()
    if Codigo == 100:
        conta += float(Quantidade) * 1.20
    elif Codigo == 101:
        conta += float(Quantidade) * 1.30
    elif Codigo == 102:
        conta += float(Quantidade) * 1.50
    elif Codigo == 103:
        conta += float(Quantidade) * 1.20
    elif Codigo == 104:
        conta += float(Quantidade) * 1.70
    elif Codigo == 105:
        conta += float(Quantidade) * 2.20
    else:
        conta = conta + float(Quantidade) * 1.00

    i = input('Vai pedir de novo (s/n)? ')
    while i != 'n' and i != 's':
        i = input('Entrada inválida! Vai pedir de novo (s/n)? ')

print(f'A conta final é: R$ {conta}')
