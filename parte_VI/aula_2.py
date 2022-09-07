# Módulos úteis 2

# Biblioteca random: https://docs.python.org/3/library/random.html

import random

print(random.random()) # números entre zero e um
print(random.randint(1,10)) # números entre um e dez
print(random.randrange(0, 10, 2)) # números zero um e dez com quebra de 2 (divisores de 2)
print(random.randrange(0, 10, 3)) # números zero um e dez com quebra de 3 (divisores de 3)

x = ['K', 'd', 13, '34-j', 'x']
print(random.choice(x)) # elemento aleatório dentro da lista

# Biblioteca time: https://docs.python.org/3/library/time.html

import time as tm

print(tm.time())

# verifica quanto tempo o código levou para executar o loop
antes = tm.time()
lista = []
for i in range(0,10000):
  lista.append(i)
depois = tm.time()

intervalo = depois - antes
print(f'Tempo: {intervalo} segundos')

print('Finalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a próxima')