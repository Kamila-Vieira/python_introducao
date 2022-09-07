# Coleções 2

# Dicionários
coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
print(coleta)
print(coleta['Aedes aegypt'])

coleta['Rhodnius montenegrensis'] = 11
print(coleta)

coleta['Aedes aegypt'] = 20
print(coleta)

del(coleta)['Aedes albopictus']
print(coleta)

coleta['Anopheles deaneorum'] = 11
print(coleta)

print(coleta.items())
print(coleta.keys())
print(coleta.values())

coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
print(coleta2)

coleta.update(coleta2)
print(coleta)

print(coleta.items())

for especie, num_especimes in coleta.items():
  print(f'Espécie: {especie}, número de espécimes coletados: {num_especimes}')

# Conjuntos (set)

biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo', 'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')
print(biomoleculas) # tupla

print(set(biomoleculas)) # conjunto

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)
print(c3)
print(c1.difference(c2))
print(c2.difference(c1))