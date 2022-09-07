# Estruturas de repetição - for

for numero in range(1, 6):
  print(numero)

for numero in range(5, 0, -1):
  print(numero)

limite = 5
soma = 0
soma2 = limite * ( limite + 1 ) / 2 # Com a fórmula
for numero in range(1, limite + 1): # Com o for
  soma += numero

print(soma)
print(soma2)

palavra = 'sorvete'
for letra in palavra:
  print(letra)
  if letra == 'v':
    print('Achou a letra v')

for i in range(0,5):
  print(i)
  print('---')
  for j in range(0,3):
    print(j)
  print()