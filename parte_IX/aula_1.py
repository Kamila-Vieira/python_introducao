# Expressões regulares

# Função search => Encontrar as posições de padrões dentro de uma string, se estes estiverem presentes

import re

frase = 'Olá, meu número de telefone é (42)00010-0000'
reTel = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)
print(reTel)

frase = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
rePlaca = re.search('[A-Za-z]{3}-\d{4}', frase)
print(rePlaca)

email = 'Entre em contato, meu email é teste@teste.com'
reEmail = re.search('\w+@\w+\.com', email)
print(reEmail)

# Função match => Encontrar se o começo de uma string é igual a um determinado padrão

frase = 'A placa de carro que eu anotei durante a batida foi FRT-1998'
print(re.match('[A-Za-z]{3}-\d{4}', frase))

frase2 = 'FRT-1998 é a placa do carro'
print(re.match('[A-Za-z]{3}-\d{4}', frase2))

# Função findall => Encontrar todas as substring em uma string que correspondam a um padrão

frase3 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase3))

emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''

print(re.findall('\w+@\w+\.\w*', emails))
print(re.findall('[\w.+-]+@[\w-]+\.[\w.-]+', emails))
print(re.findall('\w+@\w+\.\w+.?\w+', emails))