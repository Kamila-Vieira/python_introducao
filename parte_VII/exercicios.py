""" 1. Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista 
(o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
- ValueError: se o usuário digitar um carácter
- ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
- IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
- KeyboardInterrupt: caso o usuário interrompa a execução """

# 2. Mostre uma mensagem personalizada na ocorrência de cada um desses erros

print('Versão com while: ')
print()
numeros = []

while True:
  try:
    numero1 = float(input('Digite o primeiro número: '))
    numeros.append(numero1)
  except ValueError:
    print('Valor inválido, digite somente números')
  except KeyboardInterrupt:
    print()
    print('Você interrompeu a execução')
    break
  else:
    break


while True:
  try:
    numero2 = float(input('Digite o segundo número: '))
    divisao = numeros[0] / numero2
    numeros.append(numero2)
    divisao = numeros[0] / numeros[1]
  except IndexError:
    print('É necessário inserir os dois numeros!')
    try:
      numero1 = float(input('Insira o primeiro número novamente: '))
      numeros.append(numero1)
    except ValueError:
      print('Valor inválido, digite somente números')
    except KeyboardInterrupt:
      print()
      print('Você interrompeu a execução')
      break
  except ZeroDivisionError:
    print('Valor inválido, o segundo número não pode ser zero')
  except ValueError:
    print('Valor inválido, digite somente números')
  except KeyboardInterrupt:
    print()
    print('Você interrompeu a execução')
    break
  else:
    print(f'O valor da divisão dos números é {divisao}')
    break
    
print('Versão do professor: ')
print()

lista = []
try:
  lista.append(float(input('Digite o primeiro valor: ')))
  lista.append(float(input('Digite o segundo valor: ')))
  divisao = lista[0] / lista[1]
except ValueError:
  print('Erro! Valor inválido')
except ZeroDivisionError:
  print('Erro! Divisão por zero')
except IndexError:
  print('Erro! Índice inválido')
except KeyboardInterrupt:
  print('Usuário interrompeu a execução')
else:
  print(f'A divisão é {divisao}')