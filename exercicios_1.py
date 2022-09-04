# 1. Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

num_a = int(input('Digite o primeiro número: '))
num_b = int(input('Digite o segundo número: '))

print(f'A soma de {num_a} e {num_b} é {num_a + num_b}')
print(f'A subtração de {num_a} e {num_b} é {num_a - num_b}')
print(f'A multiplicação de {num_a} e {num_b} é {num_a * num_b}')
print(f'A divisão de {num_a} e {num_b} é {round(num_a / num_b, 2)}')

""" 2. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. 
O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem """

km = 12
tempo_gasto = float(input('Digite o tempo gasto na viagem: '))
velocidade_media = float(input('Digite a velocidade média: '))
distancia_percorrida = tempo_gasto * velocidade_media
litros_usados = distancia_percorrida / km

print('Velocidade média', velocidade_media)
print('Tempo gasto na viagem', tempo_gasto)
print('Distância percorrida', distancia_percorrida)
print('Quantidade de litros utilizados na viagem',  round(litros_usados,1))