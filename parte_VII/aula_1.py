# Tratamento de erros e exceções

""" NameError: variável nao foi definida
TypeError: tipos de dados incompatíveis
RuntimeError: erro de execução
SyntaxError: sintaxe digitada é inválida e não reconhecida pelo interpretador
ZeroDivisionError: divisão por zero
IndexError: índice está fora da coleção """

# Tipos de erros

# print(3 = 4) # SyntaxError: can't assign to literal

# print('Meu nome é', nome) # NameError: name 'nome' is not defined

# print(3 / 0) # ZeroDivisionError: division by zero

# print(2.3 / 'cachorro') # TypeError: unsupported operand type(s) for /: 'float' and 'str'

c = [1,2,3,4,5]

# print(c[5]) # IndexError: list index out of range

# int(input('Digite um núm2ero inteiro: ')) # Ao digitar algo diferente de número inteiro: ValueError: invalid literal for int() with base 10: 'texto'

# Tratamento de erros

try:
  n = int(input('Digite um número inteiro: '))
except:
  print('Valor inválido')
else:
  print(f'Valor digitado é {n}')

while True:
  try:
    n = int(input('Digite um número inteiro: '))
  except:
    print('Valor inválido')
  else:
    print(f'Valor digitado é {n}')
    break

while True:
  try:
    p = int(input('Digite um número inteiro: '))
  except ValueError:
    print('Valor inválido')
  except KeyboardInterrupt:
    print()
    print('Usuário interrompeu a execução')
    break
  else:
    print(f'Valor digitado é {p}')
    break