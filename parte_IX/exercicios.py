# Metacaractereres:

# . -> Qualquer (exceto nova linha)
# \w -> Qualquer alfa
# \W -> Qualquer não alfa
# \d -> Qualquer digito
# \D -> Qualquer não digito
# \s -> Espaço em branco
# ^ -> Começa com
# $ -> Termina com
# \ -> Especificar significa literal de algum caractere reservado

# Quantificadores:
# [] -> Opcional entre os que estiverem em colchetes
# () -> Grupos de caracteres
# * -> Zero ou mais ocorrencias
# ? -> uma ou mais ocorrencias
# {m,n} -> de m a n ocorrencias
# | -> ou

# 1. Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
import re

texto = "Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e 11111-111 meu site é https://www.iaexpert.academy http://iaexpert.com.br"

# - Números
numeros = re.findall('\d', texto)
print(numeros)

# - CEPs
ceps = re.findall('\d{5}-\d{3}', texto)
print(ceps)

# - URLs
urls = re.findall('https?://[\w\.]+', texto)
print(urls)
