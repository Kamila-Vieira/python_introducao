# Manipulação de arquivos

path = 'parte_VIII/content/'

with open(f'{path}frase1.txt', 'r') as tex:
  for linha in tex:
    print(linha)

with open(f'{path}frase1.txt') as tex:
  r = tex.readlines()
print(r)

with open(f'{path}texto2.txt', 'w') as texto:
  texto.write('Olá a todos')

with open(f'{path}texto2.txt', 'r') as tex:
  for linha in tex:
    print(linha)