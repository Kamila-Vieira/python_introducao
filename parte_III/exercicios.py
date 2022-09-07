# 1. Ler 5 notas e informar a média

print('Com For ------------------')

notas = 5
nota = soma_notas = media = 0

for numero in range(1, notas + 1):
  nota = float(input(f'Insira a nota {numero}: '))
  soma_notas += nota

media = soma_notas / notas

print(f'A média é de {media}')
print()
print('Com while ------------------')

numero = 1
nota = soma_notas = media = 0

while numero <= notas:
  nota = float(input(f'Insira a nota {numero}: '))
  soma_notas += nota
  numero += 1

media = soma_notas / notas

print(f'A média é de {media}')
print()

# 2. Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
numero_tabuada = 3
limite = 10

print(f'Tabuada do {numero_tabuada}:')
print('Com For ------------------')

for numero in range(1, limite + 1):
  valor = numero_tabuada * numero
  print('{} x {} = {}'.format(numero_tabuada, numero, valor)) # equivale à print(f'{numero_tabuada} x {numero} = {valor}')

print()
print('Com while ------------------')

numero = 1
while numero <= limite:
  print('{} x {} = {}'.format(numero_tabuada, numero, numero_tabuada * numero))
  numero += 1