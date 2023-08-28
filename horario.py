from datetime import datetime, timezone, timedelta
from emoji import emojize

fuso = timezone(timedelta(hours=-3))
horario_horas = int(datetime.now().time().strftime('%H'))

horario_fuso = datetime.now().astimezone(fuso)

horario_atual = horario_fuso.strftime('%H:%M')
horario_minutos = int(horario_fuso.strftime('%M'))

nome = input('Qual o seu nome? ')

if (horario_horas >= 0 and horario_horas < 12 ):
     print(emojize(f'Bom dia {nome}!! :sun:'))
elif (horario_horas >= 12 and horario_horas < 18):
    print (emojize(f'Boa tarde {nome}!! :sun_behind_cloud:'))
else:
     print(emojize(f'Boa noite {nome}!! :last_quarter_moon_face:'))

meio_dia_hora = int(12)
dia_minutos = int(60)
tarde_hora = int(18)

diferenca_hora = meio_dia_hora - horario_horas
diferenca_hora1 = tarde_hora - horario_horas
diferenca_minuto = dia_minutos - horario_minutos

#Quanto tempo falta até o meio-dia

if (diferenca_hora == 0 and diferenca_minuto == 60) :
    print('Já são meio-dia')
elif(diferenca_hora > 1 and diferenca_minuto == 60) :
    diferenca_hora = diferenca_hora
    if (diferenca_hora1 == 1) :
        print('Falta {} hora até o meio-dia'.format(diferenca_hora))
    else :
        print('Faltam {} horas até o meio-dia'.format(diferenca_hora))
elif(diferenca_hora > 1 and diferenca_minuto < 60):
    diferenca_hora = diferenca_hora - 1
    if (diferenca_hora == 1) :
        print('Falta {} hora e {} minutos até o meio-dia'.format(diferenca_hora, diferenca_minuto))
    else :
        print('Faltam {} horas e {} minutos até o meio-dia'.format(diferenca_hora, diferenca_minuto))
elif(diferenca_hora == 1 and diferenca_minuto < 60):
    if(diferenca_minuto == 1):
        print('Falta {} minuto para o meio-dia'.format(diferenca_minuto))
    else:
        print ('Faltam {} minutos até o meio-dia'.format(diferenca_minuto))
else:
    print

#Quanto tempo falata até a noite chegar

if (horario_horas >= 12 and diferenca_hora1 == 0 and diferenca_minuto == 60) :
    print('Agora são 18 horas, está começando a noite!!')
elif(horario_horas >= 12 and diferenca_hora1 >= 1 and diferenca_minuto == 60):
    diferenca_hora1 = diferenca_hora1
    if (diferenca_hora1 == 1) :
        print('Falta {} hora até a noite'.format(diferenca_hora1))
    else :
        print('Faltam {} horas até a noite'.format(diferenca_hora1))
elif(horario_horas >= 12 and diferenca_hora1 > 1 and diferenca_minuto < 60) :
    diferenca_hora1 = diferenca_hora1 - 1
    if (diferenca_hora1 == 1) :
        print('Falta {} hora e {} minutos até a noite'.format(diferenca_hora1, diferenca_minuto))
    else :
        print('Faltam {} horas e {} minutos até a noite'.format(diferenca_hora1, diferenca_minuto))
elif (horario_horas >= 12 and diferenca_hora1 == 1 and diferenca_minuto < 60) :
    if (diferenca_minuto == 1) :
        print('Falta {} minuto até a noite'.format(diferenca_minuto))
    else:
        print('Faltam {} minutos até a noite'.format(diferenca_minuto))
else:
    print

print('No horário de Brasília são: {}'.format(horario_atual))

