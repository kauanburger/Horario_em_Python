from datetime import datetime, timezone, timedelta

fuso = timezone(timedelta(hours=-3))
horario_horas = int(datetime.now().time().strftime('%H'))

horario = datetime.now().astimezone(fuso)

horario2 = horario.strftime('%H:%M')
horario3 = int(horario.strftime('%H'))
horario4 = int(horario.strftime('%M'))

nome = input('Qual o seu nome? ')

if (horario_horas >= 0 and horario_horas < 12 ):
    print(f'Bom dia {nome} !!')
elif (horario_horas >= 12 and horario_horas < 18):
    print (f'Boa tarde {nome}!!')
else:
    print(f'Boa noite {nome}!!')

meio_dia_hora = int(12)
meio_dia_minutos = int(60)

diferenca_hora = (meio_dia_hora - horario3) - 1
diferenca_minuto = meio_dia_minutos - horario4

if (diferenca_hora == 0 and diferenca_minuto == 60) :
    print('Já são meio-dia')
elif(diferenca_hora > 1 and diferenca_minuto == 60) :
    diferenca_hora = diferenca_hora + 1
    print('Faltam {} horas até o meio-dia'.format(diferenca_hora))
elif(diferenca_hora > 0 and diferenca_minuto < 60):
    print('Faltam {} minutos para meio-dia'.format(diferenca_minuto))


print('No horário de Brasília são: {}'.format(horario2))

