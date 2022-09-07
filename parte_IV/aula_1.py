# Coleções

# tuplas
tupla = ('Homo sapiens', 'Canis familiaris', 'Felis catus')
print(tupla)
print(tupla[0])
print(tupla[0:2])
print(tupla.index('Canis familiaris'))

for elemento in tupla:
  print(elemento)

# Listas
lista_1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
lista_2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']
lista_3 = lista_1 + lista_2
print(lista_1)
print(lista_2)
print(lista_3)

lista_2_2 = lista_2 * 2
print(lista_2_2)

print(lista_1[0])
print(lista_1[0:2])
print(lista_1[2:])

lista_1.append('Gorila gorila')
print(lista_1)

lista_1.remove('Felis catus')
print(lista_1)

del(lista_1) # deletar lista
# print(lista_1)

for item in lista_2_2:
  print(item)