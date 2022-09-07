# Módulos úteis

# Biblioteca math: https://docs.python.org/3/library/math.html

import math

raiz_nove = math.sqrt(9)
print(raiz_nove)

seno_qc = math.sin(45)
cosseno_qc = math.cos(45)
print(seno_qc)
print(cosseno_qc)

log = math.log(1000, 10) # lê-se logaritmo de 1000 na base 10
log2 = math.log(32, 2)

print(log)
print(log2)

log3 = math.log(1000) # Neste caso a base quando implícita é o número de euler "math.e"
log4 = math.log(1000, math.e)
print(log3)
print(log4)
# Sendo assim log3 == log4
print(log3 == log4) # True

print(math.e)
print(math.pi)

# Biblioteca datetime: https://docs.python.org/3/library/datetime.html

import datetime

print(dir(datetime))

hoje = datetime.date.today()
agora = datetime.datetime.now()
print(hoje)
print(agora)

data = datetime.date(2020, 7, 10)
dia = data.day
mes = str(data.month).zfill(2) # Fixa o mês em duas casas
ano = data.year
print(data)
print(f'{dia}/{mes}/{ano}')

horario = datetime.datetime(2020, 7, 10, 8, 30, 0)
hora = horario.hour
minuto = horario.minute
segundo = horario.second
hora_texto = 'hrs' if hora > 1 else 'hr' # condicional inline (if ternário)

print(horario)
print(f'{hora}{hora_texto} {minuto}m {segundo}s')