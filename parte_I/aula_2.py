# Manipulação de strings
a = 'casaco'
print(a)

maiuscula = a.upper()
print(maiuscula)

minuscula = maiuscula.lower()
print(minuscula)

capital = a.capitalize()
print(capital)

indice_metade_palavra = int(len(a) / 2) #Importante que seja int

metade_palavra = a[0:indice_metade_palavra]
print(metade_palavra)

ultimas_letras = a[indice_metade_palavra:]
print(ultimas_letras)

b = a.replace('aco', 'inha')
print(a)
print(b)

c = a.replace('a', 'o')
print(c)

print(b.find('s'))

print(b.find('a'))

print(b.find('b'))

e = ' casaco '
print(len(e))

f = e.strip()
print(f)

n1 = 14
n2 = 16

print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')