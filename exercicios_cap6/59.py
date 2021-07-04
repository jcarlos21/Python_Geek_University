"""
Questão 59
"""
Num_Hab_Cidade = int(input('Entre com o número de habitantes da cidade: '))
Tarifa_KWh = float(input('Entre com o valor de kilowatts por hora: '))
Consumo_Mes = 0.0
CodigoConsumidor = 0

SomaTotalHabitantes = 0
MenorConsumo = 1000000000000000000000000000000000000
MaiorConsumo = -20000000000
MediaConsumo = 0
SomaTotalResidencial = 0
SomaTotalComercial = 0
SomaTotalIndustrial = 0

for i in range(0, Num_Hab_Cidade):
    Consumo_Mes = float(input(f'Entre com o consumo mensal de kilowatts do {i+1}° habitante: '))
    CodigoConsumidor = int(input('Entre com o código do consumidor: '
                                 '\n1 - Residencial'
                                 '\n2 - Comercial'
                                 '\n3 - Industrial'
                                 '\nOpçção: '))

    SomaTotalHabitantes += Consumo_Mes
    if Consumo_Mes > MaiorConsumo:
        MaiorConsumo = Consumo_Mes
    if Consumo_Mes < MenorConsumo:
        MenorConsumo = Consumo_Mes

    if CodigoConsumidor == 1:
        SomaTotalResidencial += Consumo_Mes
    elif CodigoConsumidor == 2:
        SomaTotalComercial += Consumo_Mes
    else:
        SomaTotalIndustrial += Consumo_Mes

MediaConsumo = SomaTotalHabitantes / Num_Hab_Cidade

print(f'\nO maior e o menor consumo entre os habitante foi de {MaiorConsumo} KWh e {MenorConsumo} KWh.'
      f'\nA média de consumo entre os habitantes foi de : {MediaConsumo} KWh.'
      f'\nO consumo dos habitantes residenciais foi de: {SomaTotalResidencial}.'
      f'\nO consumo dos habitantes comerciais foi de: {SomaTotalComercial}.'
      f'\nO consumo dos habitantes industriais foi de: {SomaTotalIndustrial}.')
