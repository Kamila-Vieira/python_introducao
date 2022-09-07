import numpy as np

""" 1. Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. 
Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados """

lista_soma = []

numero = soma = 0

while numero < 5:
    inteiro = int(input('Digite um número inteiro: '))
    lista_soma.append(inteiro)
    numero += 1

print(lista_soma)

for i in range(0, len(lista_soma)):
    soma += lista_soma[i]

print('Soma:', soma)

# Outra alternativa:
soma = np.array(lista_soma).sum()
print('Soma:', soma)

""" 2. Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. 
Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média """

alunos = {}
numero = soma = media = 0

while numero < 3:
    nome = str(input('Digite o nome do aluno: '))
    nota = float(input('Digite a nota do aluno: '))
    alunos[nome] = nota
    numero += 1

print(alunos)

for nota in alunos.values():
    soma += nota

media = soma / 3
print('A média é', media)

# 3. Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
[linhas, colunas] = matriz.shape
soma = 0

for linha in range(linhas):
    for coluna in range(colunas):
        soma += matriz[linha][coluna]

print(soma)