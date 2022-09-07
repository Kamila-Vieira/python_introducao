""" 1. Leia a idade do usuário e classifique-o em:
- Criança – 0 a 12 anos
- Adolescente – 13 a 17 anos
- Adulto – acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida """

idade = int(input('Insira sua idade: '))

if idade >= 0 and idade <= 12:
  print('Criança')
elif idade > 13 and idade <= 18:
  print('Adolescente')
elif idade > 18:
  print('Adulto')
else: 
  print('A idade é inválida')

""" 2. Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. 
Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
- Se a média for maior do que 6.0, o aluno está aprovado
- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado """

nota_M1 = float(input('Insira a nota M1: '))
nota_M2 = float(input('Insira a nota M2: '))
nota_M3 = float(input('Insira a nota M3: '))

media = (nota_M1 + nota_M2 + nota_M3) / 3

if (media >= 0.0) and (media <= 4.0):
  print('Reprovado')
elif (media >= 4.1) and (media <= 6.0):
    print('Pegou exame')
    nota_exame = float(input('Insira a nota do exame: '))
    if nota_exame > 6.0:
      print('Aprovado')
    else: 
      print('Reprovado')
elif media > 6.0:
  print('Aprovado')