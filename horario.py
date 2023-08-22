from datetime import datetime, timezone, timedelta

fuso = timezone(timedelta(hours=-3))
horario_horas = int(datetime.now().time().strftime('%H'))
horario = datetime.now().astimezone(fuso)
horario2 = horario.strftime('%H:%M')
nome = input('Qual o seu nome? ')

if (horario_horas >= 0 and horario_horas < 12 ):
    print(f'Bom dia {nome} !!')
elif (horario_horas >= 12 and horario_horas < 18):
    print (f'Boa tarde {nome}!!')
else:
    print(f'Boa noite {nome}!!')

print('No horário de Brasília são: {}'.format(horario2))