""" 1. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
- Função para ler e retorna o valor da temperatura (não recebe parâmetro)
- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
- Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão """

def le_temperatura(): 
    temperatura = float(input('Digite a temperatura em graus Celsius: '))
    temperatura_convertida = converte_temperatura(temperatura)
    return temperatura_convertida

def converte_temperatura(temperatura):
    fahrenheit = (9 * temperatura + 160) / 5
    return fahrenheit

def mostra_temperatura(valor):
    print('A temperatura em Fahrenheit é', valor)

valor = le_temperatura()
mostra_temperatura(valor)

""" 2. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. 
O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado) """

def le_tempo_velocidade(): 
    tempo = float(input('Digite o tempo: '))
    velocidade = float(input('Digite a velocidade: '))
    return tempo, velocidade

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade

def calcula_quantidade_litros(distancia):
    return distancia / 12

def mostra_valores(tempo, velocidade, distancia, litros):
    print('O tempo gasto foi de', tempo)
    print('A velocidade média foi de', velocidade)
    print('A distância percorrida foi', distancia)
    print('A quantidade de litros utilizada na viagem foi de', litros)

[tempo, velocidade] = le_tempo_velocidade()
distancia = calcula_distancia(tempo, velocidade)
quantidade_litros = calcula_quantidade_litros(distancia)
mostra_valores(tempo, velocidade, distancia, quantidade_litros)