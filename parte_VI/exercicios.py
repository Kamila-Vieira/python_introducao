""" 1. Crie um arquivo .py com duas funções
- Função para ler um string (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)
- Função para ler um número float (recebe como parâmetro uma mensagem e retorna o que o usuário digitou) """

import leitura as lt

texto = lt.le_string('Digite algo: ')
print(texto)
flutuante = lt.le_float('Digite um número flutuante: ')
print(flutuante)