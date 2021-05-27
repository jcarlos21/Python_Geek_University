"""
Questão 49
"""
"""print('Entre com um horário:')
hora = input('Entre com um horário (separe as horas, os minuitos e os segundos com ":": ')
i = 0
HoraI = []

while i < len(hora):
    if (i != 2) and (i != 5):
        HoraI.append(int(hora[i]))
    i += 1

print(HoraI)

while HoraI[0] > 2 or HoraI[0] < 0 or HoraI[1] > 3 or HoraI[1] < 0 or HoraI[2] > 5 or HoraI[2] < 0 or HoraI[3] > 9 or HoraI[3] < 0 or HoraI[4] > 5 or HoraI[4] < 0 or HoraI[5] > 9 or HoraI[5] < 0:
    hora = input('Formato de hora inválida, digite novamente: ')"""

print('Entre com a hora incial do experimento: ')

hora = int(input('Entre com a hora: '))
minutos = int(input('Entre com os minutos: '))
segundos = int(input('Entre com os segundos: '))

duração = int(input('Entre com a duração do experimento em segundos: '))

horaf = (duração // 3600) + hora
minutosf = ((duração % 3600) // 60) + minutos
segundosf = ((duração % 3600) % 60) + segundos

print(f'A hora de termino é: {horaf}:{minutosf}:{segundosf}')