"""
Questão 37
"""
# é preciso pôr as verificações

HoraC = int(input('Entre com a hora de chegada: '))
HoraS = int(input('Entre com a hora de saída: '))
HoraChegada = []
HoraSaida = []

HoraChegada.append(HoraC // 100)
HoraChegada.append(HoraC % 100)

HoraSaida.append(HoraS // 100)
HoraSaida.append(HoraS % 100)


def SubtraçãoHora(l1, l2):
    h = l2[0] - l1[0]
    m = l2[1] - l1[1]
    if h < 0:
        return 1440 + (h * 60) + m
    elif h == m == 0:
        return 1440
    else:
        return (h * 60) + m


print(f'\nTempo no estacionamento (em minutos): {SubtraçãoHora(HoraChegada, HoraSaida)} minutos')

if 0 < SubtraçãoHora(HoraChegada, HoraSaida) <= 120:
    if SubtraçãoHora(HoraChegada, HoraSaida) % 60 == 0:
        print(f'O valor cobrado é: R$ {(SubtraçãoHora(HoraChegada, HoraSaida) // 60) * 1.00}')
    else:
        print(f'O valor cobrado é: R$ {((SubtraçãoHora(HoraChegada, HoraSaida) // 60) + 1) * 1.00}')
elif 120 < SubtraçãoHora(HoraChegada, HoraSaida) <= 240:
    if SubtraçãoHora(HoraChegada, HoraSaida) % 60 == 0:
        print(f'O valor cobrado é: R$ {(SubtraçãoHora(HoraChegada, HoraSaida) // 60) * 1.40}')
    else:
        print(f'O valor cobrado é: R$ {((SubtraçãoHora(HoraChegada, HoraSaida) // 60) + 1) * 1.40}')
else:
    if SubtraçãoHora(HoraChegada, HoraSaida) % 60 == 0:
        print(f'O valor cobrado é: R$ {(SubtraçãoHora(HoraChegada, HoraSaida) // 60) * 2.00}')
    else:
        print(f'O valor cobrado é: R$ {((SubtraçãoHora(HoraChegada, HoraSaida) // 60) + 1) * 2.00}')
